from django.db import models
from user.models import Participant
from django.db.models.deletion import CASCADE


# Create your models here.
class Data(models.Model):
    username = models.ForeignKey('user.Participant', on_delete=CASCADE)
    sensor_id = models.CharField(max_length=15)
    timestamp = models.BigIntegerField()
    accuracy = models.IntegerField()
    data = models.CharField(max_length=16)
    device = models.CharField(max_length=32)
