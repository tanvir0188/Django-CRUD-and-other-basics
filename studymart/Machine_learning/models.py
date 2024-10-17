from django.db import models

# Create your models here.
class Teachers(models.Model):
    tid = models.IntegerField()
    tname = models.CharField(max_length=40)
    tmails = models.CharField(max_length=50)
