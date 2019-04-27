from django.db import models


# Create your models here.
class Participant(models.Model):
    username = models.CharField(max_length=16, primary_key=True)
    password = models.CharField(max_length=16)
