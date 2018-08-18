import string
import requests
import tempfile
import json
from .models import Analytics, Photos, PhotoTags, GroupPhotos, PhotoDetails
from django.conf import settings as GlobalSettings
from django.core import files

from celery import shared_task

@shared_task
def update_user_clicks(user, token):
    try:
        analytics = Analytics.objects.get(token=token)
        analytics.click = analytics.click + 1
        analytics.save()

    except Analytics.DoesNotExist:
        Analytics.objects.create(user_id = user, token = token, click = 1)
    return 'created'

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

@shared_task
def get_group_photos_ids(flickr_id, group_id):

    data = get_group_photos(1, flickr_id)
    for photo in data['photos']['photo']:
        photoobj = Photos.objects.create(flickr_id = photo['id'], owner = photo['ownername'], date = photo['dateadded'], server = photo['server'], farm = photo['farm'], title = photo['title'], secret = photo['secret'])
        get_photo_tags.delay(photoobj.id)
        url = 'https://farm'+str(photo['farm'])+'.staticflickr.com/'+str(photo['server'])+'/'+str(photo['id'])+'_'+photo['secret']+'_b.jpg'
        download_photo.delay(url, photoobj.id)
        GroupPhotos.objects.create(group_id = group_id, photo = photoobj)

    pages = data['photos']['pages']
    if pages > 1:
        for i in range(2, pages+1):
            data = get_group_photos(i, flickr_id)
            for photo in data['photos']['photo']:
                photoobj = Photos.objects.create(flickr_id = photo['id'], owner = photo['ownername'], date = photo['dateadded'], server = photo['server'], farm = photo['farm'], title = photo['title'], secret = photo['secret'])
                get_photo_tags.delay(photoobj.id)
                url = 'https://farm'+str(photo['farm'])+'.staticflickr.com/'+str(photo['server'])+'/'+str(photo['id'])+'_'+photo['secret']+'_b.jpg'
                download_photo.delay(url, photoobj.id)
                GroupPhotos.objects.create(group_id = group_id, photo = photoobj)

    return 'download started'


@shared_task
def download_photo(url, id):

    result = requests.get(url, stream=True)
    photoobj = Photos.objects.get(id=id)
    if result.status_code == requests.codes.ok:
        lf = tempfile.NamedTemporaryFile()

        file_name = url.split('/')[-1]
        for block in result.iter_content(1024 * 8):
            if not block:
                break

            lf.write(block)
        photoobj.image.save(file_name, files.File(lf))

    return 'downloaded'

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

@shared_task
def get_photo_tags(id):

    photo = Photos.objects.get(id=id)
    data = get_photo_info(photo.flickr_id)
    print(data['photo']['comments']['_content'])
    PhotoDetails.objects.create(photo=photo, description=data['photo']['description']['_content'], comments_count = data['photo']['comments']['_content'], views_count = data['photo']['views'])
    for tag in data['photo']['tags']['tag']:
        phototags = PhotoTags.objects.create(photo=photo, tag=tag['_content'])
    return 'Photo info fetched'
