from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    # Add any additional fields you want for your user model
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    bio = models.TextField()
    location = models.CharField(max_length=255)
    notification = models.BooleanField(default=False)

    # You can also add any custom methods or properties specific to your user model
    # For example:
    # def get_full_name(self):
    #     return f"{self.first_name} {self.last_name}"
