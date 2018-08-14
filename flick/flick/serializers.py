from rest_framework import serializers
from .models import Groups, Photos, PhotoUrls, PhotoTags, GroupPhotos


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ('id', 'name')
