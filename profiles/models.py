from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    A custom user model that extends Django's built-in 'AbstractUser' class to include additional 
    fields for enhanced user information and location data.

    Fields:
    - home_address (CharField): A character field for storing the user's home address.
    - phone_number (CharField): A character field for storing the user's phone number.
    - location (PointField): A geometric point field for storing the user's location. (nullable and can be left blank)
    """

    home_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    location = models.PointField(null=True, blank=True)

    def __str__(self):
        return self.username
