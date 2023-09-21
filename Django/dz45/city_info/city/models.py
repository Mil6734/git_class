from django.db import models


class City(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    image = models.ImageField(upload_to='city/images/')
