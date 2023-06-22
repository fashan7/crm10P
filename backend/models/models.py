from django.db import models

# Create your models here.
class Models(models.Model):
    model_name = models.CharField(max_length=255)
    associated_with_training = models.ForeignKey('Training', on_delete=models.CASCADE)