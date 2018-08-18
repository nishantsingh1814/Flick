from rest_framework import serializers
from .models import Groups, Photos, PhotoTags, GroupPhotos,  Analytics


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        fields = ('id', 'name', 'member_count', 'image_count', 'description', 'icon')

class PhotoTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoTags
        fields = ('tag',)

class PhotoSerializer(serializers.ModelSerializer):
    tags = PhotoTagSerializer(many=True, read_only=True)

    class Meta:
        model = Photos
        fields = ('id', 'owner', 'title', 'image','comments_count', 'views_count', 'description', 'tags')

class GroupPhotosSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(read_only=True)

    class Meta:
        model = Groups
        fields = ('id', 'photo')

class AnalyticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Analytics
        fields = ('click',)
