from faker import Factory
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","demo1.settings")

import django
django.setup()
from hostweb.models import *

def create_names(fake):
    stuff = [
        'user_name',
        'phone_number',
    ]
    for i in range(100):
        
        try:
            User.objects.create(
                username = fake.user_name(),
                mail = fake.email(),
                passwd = fake.password(),
                telephone = fake.phone_number(),
                Type='U'
            )
        except User.DoesNotExist:
            print("Failed")
        
        '''
        print(fake.user_name())
        print(fake.password())
        print(fake.email())
        print(fake.phone_number())
        '''

if __name__ == "__main__":
    fake = Factory.create()
    create_names(fake)