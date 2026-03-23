from django.db import models

# Create your models here.
class Count(models.Model):
    key = models.CharField(max_length=64, unique=True)
    value = models.IntegerField(default=0)