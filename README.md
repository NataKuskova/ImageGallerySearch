# Image Gallery Search

This application was built on Python 3.6 using Django 3.1.1 and Django REST Framework 3.11.1

### To deploy locally run the following commands:

1.  Create a virtual environment and activate it:
    ``` 
    $ python3 -m venv .env
    $ . .env/bin/activate
    ```
2. Install requirements:
    ```
   $ pip install -r requirements.txt
   ```
3. Run server:
    ```
   $ python manage.py runserver
   ```

### URLs

1. Django admin
    ```
    http://127.0.0.1:8000/admin
    ```
    Login: admin
    
    Password: 123456
2. All photos:
    ```
   GET http://127.0.0.1:8000/photo/
   ```
3. Search by keyword:
    ```
   GET http://127.0.0.1:8000/photo/search/{search_term}/
   e.g.: http://127.0.0.1:8000/photo/search/nikon/
   ```
