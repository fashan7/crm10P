from django.db import models

# Create your models here.
class File(models.Model):
    file_name = models.CharField(max_length=255)
    file_status = models.CharField(max_length=50)
    associated_with_lead = models.ForeignKey('Lead', on_delete=models.CASCADE)