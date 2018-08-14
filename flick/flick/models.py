from django.db import models
from django.utils import timezone
import time

class BaseModel(models.Model):
    """
    Base parent model for all the models
    """
    created_on = models.DateTimeField(blank=True, auto_now_add=True)
    updated_on = models.DateTimeField(blank=True, null=True, default=None)
    deleted = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)

    class Meta:
        abstract = True

    # Override save method.
    def save(self,  *args, **kwargs):

        self.updated_on = timezone.now()
        super(BaseModel, self).save(*args, **kwargs)

class Groups(BaseModel):
    class Meta:
        db_table = 'group'

    flickr_id = models.CharField(max_length=30, blank=False, null=False)
    name = models.CharField(max_length=255, null = False, default=None)
    member_count = models.IntegerField(default=0)
    image_count = models.IntegerField(default=0)
    description = models.TextField(blank=True)

class Photos(BaseModel):
    class Meta:
        db_table = 'photo'
    flickr_id = models.CharField(max_length=30, blank=False, null=False)
    owner = models.CharField(max_length=255, null =True, default=None)
    title = models.CharField(max_length=255, null =True, default=None)
    description = models.TextField(blank=True)
    comments_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)

class PhotoUrls(BaseModel):
    class Meta:
        db_table = 'photo_urls'
    photo = models.ForeignKey(Photos, on_delete = models.CASCADE)
    url = models.TextField(blank=True)
    size = models.CharField(max_length=30)

class PhotoTags(BaseModel):
    class Meta:
        db_table = 'photo_tags'
    photo = models.ForeignKey(Photos, on_delete = models.CASCADE)
    tag = models.TextField(blank=True)

class GroupPhotos(BaseModel):
    class Meta:
        db_table = 'group_photos'
    group = models.ForeignKey(Groups, on_delete = models.CASCADE )
    photo = models.ForeignKey(Photos, on_delete = models.CASCADE )
