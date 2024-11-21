from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)

