from django.db import models

# Create your models here.
class Elearning(models.Model):
    platform_details = models.TextField()
    associated_with_file = models.ForeignKey('File', on_delete=models.CASCADE)

