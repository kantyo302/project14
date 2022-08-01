from django.db import models


class ModelsHello(models.Model):
    title = models.CharField(max_length = 100)
    number = models.IntegerField()
# Create your models here.

class IphoneScreen(models.Model):
    title = models.CharField(max_length= 100)
    number = models.IntegerField()