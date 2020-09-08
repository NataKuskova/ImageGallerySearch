from django.db import models


class Photo(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)
    picture_id = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=100)
    camera = models.CharField(max_length=100, null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    cropped_picture = models.URLField(null=True, blank=True)
    full_picture = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ('-modified', '-created',)
