from django.db import models


class UserData(models.Model):
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=100)
