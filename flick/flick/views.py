import requests
import json
import time
import datetime
import base64

from django.shortcuts import render
from django.conf import settings as GlobalSettings
from django.db import connections


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from .models import Groups, Photos, PhotoUrls, PhotoTags, GroupPhotos
from .serializers import GroupSerializer
class DownloadGroups(APIView):

    def get(self, request, format=None):

        try:
            groupId = request.GET.get("group_id",None)

            payload = {'method':'flickr.groups.getInfo',
            'api_key':GlobalSettings.FLICKR_API_KEY,
            'group_id':groupId,
            'format':'json',
            'nojsoncallback':1
            }
            r = requests.get('https://api.flickr.com/services/rest/', params=payload)
            print(r.json())
            data = r.json()['group']
            name = data['name']['_content']
            flickr_id = data['id']
            member_count = data['members']['_content']
            image_count = data['pool_count']['_content']
            description = data['description']['_content']
            group = Groups.objects.create(name = name, flickr_id = flickr_id, member_count = member_count, image_count = image_count, description = description )
            serializer = GroupSerializer(group, context={"request": request})

            response = {'status': status.HTTP_200_OK, 'data': serializer.data}
        except ValueError as err:
            response = {'status': status.HTTP_400_BAD_REQUEST, 'error_message': str(err)}
        return Response(response, status=response['status'])


def get_group_photos(page, groupId):
    payload = {
        'method':'flickr.groups.pools.getPhotos',
        'api_key':GlobalSettings.FLICKR_API_KEY,
        'group_id':groupId,
        'format':'json',
        'nojsoncallback':1,
        'per_page':500,
        'page':page
    }
    r = requests.get(' https://api.flickr.com/services/rest/', params=payload)
    return json.loads(r.content.decode('cp1252'))

class GetGroupPhotos(APIView):

    def get(self, request, format=None):

        try:
            groupId = request.GET.get("group_id",None)

            group = Groups.objects.get(id = groupId)

            data = get_group_photos(1, group.flickr_id)

            pages = data['photos']['pages']

            if pages > 1:
                for i in range(2, pages+1):
                    data = get_group_photos(i, group.flickr_id)
                    for photo in data['photos']['photo']:
                        photo = Photos.objects.create(flickr_id = photo['id'])
                        print(photo)
                        GroupPhotos.objects.create(group = group, photo = photo)

            response = {'status': status.HTTP_200_OK, 'message': 'Group added'}
        except ValueError as err:
            print(r.json())
            response = {'status': status.HTTP_400_BAD_REQUEST, 'error_message': str(err)}

        return Response(response, status=response['status'])

def get_photo_size(id):

    payload = {
    'method':'flickr.photos.getSizes',
    'api_key':GlobalSettings.FLICKR_API_KEY,
    'photo_id':id,
    'format':'json',
    'nojsoncallback':1,
    }
    r = requests.get(' https://api.flickr.com/services/rest/', params=payload)
    return r.json()

class PhotoSizes(APIView):

    def get(self, request, format=None):

        photos = Photos.objects.all()
        for photo in photos:
            data = get_photo_size(photo.flickr_id)
            for size in data['sizes']['size']:
                photourl = PhotoUrls.objects.create(photo_id=photo.id, size = size['label'], url=size['source'])
                print(photourl)
        response = {'status': status.HTTP_200_OK, 'message': 'Image url download'}
        return Response(response, status=response['status'])

def get_photo_info(id):

    payload = {
    'method':'flickr.photos.getInfo',
    'api_key':GlobalSettings.FLICKR_API_KEY,
    'photo_id':id,
    'format':'json',
    'nojsoncallback':1,
    }
    r = requests.get(' https://api.flickr.com/services/rest/', params=payload)
    return r.json()

class PhotoInfo(APIView):

    def get(self, request, format=None):

        photos = Photos.objects.all()
        for photo in photos:
            data = get_photo_info(photo.flickr_id)
            photo.owner = data['photo']['owner']['realname']
            photo.title = data['photo']['title']['_content']
            photo.description = data['photo']['description']['_content']
            photo.comments_count = data['photo']['comments']['_content']
            photo.views_count = data['photo']['views']
            photo.save()
            for tag in data['photo']['tags']['tag']:
                phototags = PhotoTags.objects.create(photo=photo, tag=tag['_content'])
                print(phototags)
        response = {'status': status.HTTP_200_OK, 'message': 'Image Info added'}
        return Response(response, status=response['status'])

class GetGroups(APIView):
    def get(self, request, format=None):

        groups = Groups.objects.all()
        
