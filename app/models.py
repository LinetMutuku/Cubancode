import os
import uuid

from django.db import models


def unique_img_name(instance, filename):
    name = uuid.uuid4()
    print(name)

    ext = filename.split('.')[-1]
    full_name = f'{name}.{ext}'
    return os.path.join('guests', full_name)


class Guest(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    phone_number = models.IntegerField()
    number_of_guests = models.IntegerField()
    profile_picture = models.ImageField(upload_to=unique_img_name, null=True , default='guests/default.png')
    check_in = models.DateTimeField(null=True)
    check_out = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
