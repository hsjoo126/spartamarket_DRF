from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    GENDER_CHOICES = [
        ("M" , "남성"),
        ("F" , "여성")
    ]

    name = models.CharField(max_length=10)
    email =  models.EmailField()
    nickname = models.CharField(max_length=20)
    birthday = models.DateField()
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
    introduce = models.TextField()

