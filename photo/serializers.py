from rest_framework import serializers

from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = [
            'picture_id',
            'author',
            'camera',
            'tags',
            'cropped_picture',
            'full_picture'
        ]
