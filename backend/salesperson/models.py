from django.db import models

# Create your models here.
class Salesperson(models.Model):
    salesperson_name = models.CharField(max_length=255)