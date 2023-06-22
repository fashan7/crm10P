from django.db import models

# Create your models here.
class Manager(models.Model):
    manager_name = models.CharField(max_length=255)