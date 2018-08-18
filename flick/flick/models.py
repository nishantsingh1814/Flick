from django.db import models
from django.utils import timezone
import time
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser
)
from .signals import user_password_update
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

def get_image_path(instance, filename):
    return 'images/{0}_{1}'.format(str(time.time()).replace('.', ''), filename)

class User(AbstractBaseUser):

    class Meta:
        db_table = 'user'

    user_name = models.CharField(max_length=17, unique=True)
    password = models.CharField(max_length=100, blank=False, null=False)
    USERNAME_FIELD = 'user_name'

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
    icon = models.ImageField(upload_to=get_image_path, null=True)

class Photos(BaseModel):
    class Meta:
        db_table = 'photo'
    flickr_id = models.CharField(max_length=30, blank=False, null=False)
    owner = models.CharField(max_length=255, null =True, default=None)
    title = models.CharField(max_length=255, null =True, default=None)
    image = models.ImageField(upload_to=get_image_path, null=True)
    secret = models.CharField(max_length=30, null =True, default=None)
    farm = models.CharField(max_length=30, null =True, default=None)
    server = models.CharField(max_length=30, null =True, default=None)
    date = models.IntegerField(default=0)


class PhotoTags(BaseModel):
    class Meta:
        db_table = 'photo_tags'
    photo = models.ForeignKey(Photos, related_name='tags', on_delete = models.CASCADE)
    tag = models.TextField(blank=True)

class PhotoDetails(BaseModel):
    class Meta:
        db_table = 'photo_details'
    photo = models.ForeignKey(Photos, related_name='details', on_delete = models.CASCADE)
    description = models.TextField(blank=True)
    comments_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)

class GroupPhotos(BaseModel):
    class Meta:
        db_table = 'group_photos'
    group = models.ForeignKey(Groups, on_delete = models.CASCADE )
    photo = models.ForeignKey(Photos, on_delete = models.CASCADE )

class Analytics(BaseModel):
    class Meta:
        db_table = 'analytics'

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    token = models.CharField(max_length=255, null =False, default=None)
    click = models.IntegerField(default=0)



@receiver(user_password_update)
def create_auth_token(sender, instance=None, **kwargs):
    token = Token.objects.filter(user=instance).delete()
    Token.objects.create(user=instance)
