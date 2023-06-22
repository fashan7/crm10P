from django.db import models

# Create your models here.
class Training(models.Model):
    training_name = models.CharField(max_length=255)
    associated_with_file = models.ForeignKey('File', on_delete=models.CASCADE)