from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

from .models import Photo
from .serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows photos to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    @api_view(['GET'])
    def search(self, search_term):
        photos = Photo.objects.filter(
            Q(picture_id=search_term) |
            Q(author__contains=search_term) |
            Q(camera__contains=search_term) |
            Q(tags__contains=search_term) |
            Q(cropped_picture__contains=search_term) |
            Q(full_picture__contains=search_term)
        )
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(photos, self)
        if page:
            serializer = PhotoSerializer(page, many=True)
        else:
            serializer = PhotoSerializer(photos, many=True)
        return paginator.get_paginated_response(serializer.data)
