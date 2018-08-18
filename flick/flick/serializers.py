from rest_framework import serializers
from .models import Groups, Photos, PhotoTags, GroupPhotos,  Analytics, PhotoDetails


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        fields = ('id', 'name', 'member_count', 'image_count', 'description', 'icon')

class PhotoTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoTags
        fields = ('tag',)

class PhotoDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoDetails
        fields = ('description', 'comments_count', 'views_count')

class PhotoSerializer(serializers.ModelSerializer):
    details = PhotoDetailsSerializer(many=True, read_only=True)
    tags = PhotoTagSerializer(many=True, read_only=True)

    class Meta:
        model = Photos
        fields = ('id', 'owner', 'title', 'image', 'tags', 'details')

class GroupPhotosSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(read_only=True)

    class Meta:
        model = Groups
        fields = ('id', 'photo')

class AnalyticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Analytics
        fields = ('click',)
