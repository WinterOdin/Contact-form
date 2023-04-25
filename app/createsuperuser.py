"""
You can put this in command in your docker-compose environment
but i prefer using

docker-compose exec app python manage.py createsuperuser
same goes for migrations
"""


from django.db import IntegrityError
from django.contrib.auth.models import User

import environ 
env = environ.Env(
    DEBUG=(bool, False)
)

try:
    superuser = User.objects.create_superuser(
        username=env('SUPER_USER_NAME', default="admin1"),
        email=env('SUPER_USER_EMAIL', default="admin1@gmail.com"),
        password=env('SUPER_USER_PASSWORD', default="admin1"))
    superuser.save()
except IntegrityError:
    print(f"Super User with username {env('SUPER_USER_NAME')} is already exit!")
except Exception as e:
    print(e)