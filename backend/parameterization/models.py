from django.db import models

# Create your models here.
class Parameterization(models.Model):
    parameterization_details = models.TextField()
    associated_with_training = models.ForeignKey('Training', on_delete=models.CASCADE)
