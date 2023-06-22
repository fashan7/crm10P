from django.db import models

# Create your models here.
class Tracking(models.Model):
    tracking_details = models.TextField()
    associated_with_lead = models.ForeignKey('Lead', on_delete=models.CASCADE)
