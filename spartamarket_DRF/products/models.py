from django.db import models
from django.conf import settings


class Products(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()