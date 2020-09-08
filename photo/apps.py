import sys

from django.apps import AppConfig


class PhotoConfig(AppConfig):
    name = 'photo'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True
        from .service import ImageService
        try:
            image_service = ImageService()
        except Exception as e:
            pass
            # need to add logging and log this exception
        else:
            image_service.load_images()
        return True
