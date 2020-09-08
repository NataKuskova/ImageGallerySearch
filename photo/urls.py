from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.PhotoViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^search/(?P<search_term>[\w:|-]+)/$', views.PhotoViewSet.search, name='photo_search'),
]
