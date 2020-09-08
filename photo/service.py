import json
import requests

from django.conf import settings

from .serializers import PhotoSerializer


class ImageService:

    def __init__(self):
        self.api_key = getattr(settings, 'SERVICE_API_KEY', None)
        self.base_url = getattr(settings, 'SERVICE_BASE_URL', None)
        if not self.api_key or not self.base_url:
            raise Exception('SERVICE_API_KEY or SERVICE_BASE_URL is not defined')
        self.auth_token = self.get_auth_token()
        if not self.auth_token:
            return
        self.headers = {
            'Authorization': f'Bearer {self.auth_token}'
        }

    def get_auth_token(self):
        data = {
            'apiKey': self.api_key
        }
        response = requests.post(f'{self.base_url}/auth', json=data)
        if response.status_code == requests.codes.ok:
            response_dict = json.loads(response.text)
            if 'token' in response_dict:
                return response_dict['token']
        return

    def load_images(self):
        images = self.get_images_by_page()
        for image in images:
            if 'id' not in image:
                continue
            self.get_image_info(image['id'])

    def get_images_by_page(self, page=1):
        response = requests.get(f'{self.base_url}/images?page={page}', headers=self.headers)
        if response.status_code == requests.codes.ok:
            response_dict = json.loads(response.text)
            if 'pictures' in response_dict:
                return response_dict['pictures']
        # check if the error is because of invalid token then request a new token
        # implement getting images from all pages
        return

    def get_image_info(self, image_id):
        response = requests.get(f'{self.base_url}/images/{image_id}', headers=self.headers)
        if response.status_code == requests.codes.ok:
            response_dict = json.loads(response.text)
            response_dict['picture_id'] = response_dict.pop('id')
            serializer = PhotoSerializer(data=response_dict)
            if serializer.is_valid():
                serializer.save()
        # add handling errors
