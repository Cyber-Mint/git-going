from django.db import models


# Create your models here.
class MyModel(models.Model):
    data = models.CharField(max_length=12)
