import requests
import json
import time
import datetime
import base64
import tempfile

from django.core import files
from django.shortcuts import render
from django.conf import settings as GlobalSettings
from django.db import connections


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.settings import api_settings


from .models import Groups, Photos, PhotoTags, GroupPhotos
from .serializers import GroupSerializer, PhotoSerializer, GroupPhotosSerializer

class PaginationAPIView(APIView):
    """
    APIView to be used for paginated responses
    """

    # The style to use for queryset pagination.
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


class DownloadGroups(APIView):

    def get(self, request, format=None):

        try:
            groupIds = ['694160@N25', '1135960@N20','52240714666@N01','78842177@N00','12512756@N00']
            for groupId in groupIds:
                payload = {'method':'flickr.groups.getInfo',
                'api_key':GlobalSettings.FLICKR_API_KEY,
                'group_id':groupId,
                'format':'json',
                'nojsoncallback':1
                }
                r = requests.get(GlobalSettings.FLICKR_BASE_URL, params=payload)
                print(r.json())
                data = r.json()['group']
                name = data['name']['_content']
                flickr_id = data['id']
                member_count = data['members']['_content']
                image_count = data['pool_count']['_content']
                description = data['description']['_content']


                group = Groups.objects.create(name = name, flickr_id = flickr_id, member_count = member_count, image_count = image_count, description = description )
                url = 'http://farm'+str(data['iconfarm'])+'.staticflickr.com/'+str(data['iconserver'])+'/buddyicons/'+str(data['nsid'])+'.jpg'
                print(group.id)
                result = requests.get(url, stream=True)
                if result.status_code == requests.codes.ok:
                    lf = tempfile.NamedTemporaryFile()

                    file_name = url.split('/')[-1]
                    for block in result.iter_content(1024 * 8):
                        if not block:
                            break

                        lf.write(block)
                    group.icon.save(file_name, files.File(lf))



            response = {'status': status.HTTP_200_OK, 'data': 'groups downloaded'}
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
    r = requests.get(GlobalSettings.FLICKR_BASE_URL, params=payload)
    return json.loads(r.content.decode('cp1252'))


def get_photo_size(id):

    payload = {
    'method':'flickr.photos.getSizes',
    'api_key':GlobalSettings.FLICKR_API_KEY,
    'photo_id':id,
    'format':'json',
    'nojsoncallback':1,
    }
    r = requests.get(GlobalSettings.FLICKR_BASE_URL, params=payload)
    return r.json()

class GetGroupPhotos(APIView):

    def get(self, request, format=None):

        try:
            groupId = request.GET.get("group_id",None)

            group = Groups.objects.get(id = groupId)

            data = get_group_photos(1, group.flickr_id)

            pages = data['photos']['pages']
            for photo in data['photos']['photo']:
                photo = Photos.objects.create(flickr_id = photo['id'])
                sizes = get_photo_size(photo.flickr_id)
                url = sizes['sizes']['size'][-1]['source']
                result = requests.get(url, stream=True)
                if result.status_code == requests.codes.ok:
                    lf = tempfile.NamedTemporaryFile()

                    file_name = url.split('/')[-1]
                    for block in result.iter_content(1024 * 8):
                        if not block:
                            break

                        lf.write(block)
                    photo.image.save(file_name, files.File(lf))
                print(photo)
                GroupPhotos.objects.create(group = group, photo = photo)

            if pages > 1:
                for i in range(2, pages+1):
                    data = get_group_photos(i, group.flickr_id)
                    for photo in data['photos']['photo']:
                        photo = Photos.objects.create(flickr_id = photo['id'])
                        sizes = get_photo_size(photo['id'])
                        url = data['sizes']['size'][-1]['source']
                        result = requests.get(url, stream=True)
                        if result.status_code == requests.codes.ok:
                            lf = tempfile.NamedTemporaryFile()

                            file_name = url.split('/')[-1]
                            for block in result.iter_content(1024 * 8):
                                if not block:
                                    break

                                lf.write(block)
                            photo.image.save(file_name, files.File(lf))
                        print(photo)
                        GroupPhotos.objects.create(group = group, photo = photo)

            response = {'status': status.HTTP_200_OK, 'message': 'Group added'}
        except ValueError as err:
            response = {'status': status.HTTP_400_BAD_REQUEST, 'error_message': str(err)}

        return Response(response, status=response['status'])


def get_photo_info(id):

    payload = {
    'method':'flickr.photos.getInfo',
    'api_key':GlobalSettings.FLICKR_API_KEY,
    'photo_id':id,
    'format':'json',
    'nojsoncallback':1,
    }
    r = requests.get(GlobalSettings.FLICKR_BASE_URL, params=payload)
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

class GetGroups(PaginationAPIView):

    def get(self, request, format=None):

        try:
            groups = Groups.objects.all()
            page = self.paginate_queryset(groups)
            if page is not None:
                serializer = GroupSerializer(page, context={"request": request}, many=True)
                return self.get_paginated_response(serializer.data)
        except RuntimeError as err:
            response = {'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'error_message': str(err)}
        return Response(response, status=response['status'])

class GetPhotos(PaginationAPIView):

    def get(self, request, format=None):

        try:
            groupId = request.GET.get('group_id',None)
            if not groupId:
                raise ValueError('group_id not found')
            photos = GroupPhotos.objects.filter(group_id=groupId)
            page = self.paginate_queryset(photos)
            if page is not None:
                serializer = GroupPhotosSerializer(page, context={"request": request}, many=True)
                return self.get_paginated_response(serializer.data)
        except ValueError as err:
            response = {'status': status.HTTP_400_BAD_REQUEST, 'error_message': str(err)}
        except RuntimeError as err:
            response = {'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'error_message': str(err)}
        return Response(response, status=response['status'])

class GetPhotoInfo(APIView):

    def get(self, request, format=None):

        try:
            photo_id = request.GET.get('photo_id', None)
            if not groupId:
                raise ValueError('photo_id not found')
            photo = Photos.objects.filter(id=photo_id)
            serializer = PhotoSerializer(photo,context = {"request": request})
            response = {'status': status.HTTP_200_OK, 'data': serializer.data}
        except ValueError as err:
            response = {'status': status.HTTP_400_BAD_REQUEST, 'error_message': str(err)}
        except RuntimeError as err:
            response = {'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'error_message': str(err)}
        return Response(response, status=response['status'])
