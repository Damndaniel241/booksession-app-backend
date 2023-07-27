from django.db import models
from .custom import customizeUser
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = None
    photo = models.ImageField(upload_to="profile")
    email = models.EmailField(unique=True)

    objects = customizeUser()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []



class Test(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    about_me = models.TextField()
    profile = models.ImageField(upload_to="profile")
