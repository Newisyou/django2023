from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Core(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)

    def click(self):
        self.coins += self.click_power
        return self
