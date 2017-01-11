from django.db import models
from django.conf import settings


class Battery(models.Model):
    nickname = models.CharField(max_length=200)
    capacity = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
