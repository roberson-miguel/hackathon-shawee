from django.db import models
from django.utils import timezone

class Participant(models.Model): 
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    specialization = models.CharField(max_length=30)
