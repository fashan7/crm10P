from django.db import models

# Create your models here.
class CallSystem(models.Model):
    call_details = models.TextField()
    associated_with_manager = models.ForeignKey('Manager', on_delete=models.CASCADE)
    associated_with_salesperson = models.ForeignKey('Salesperson', on_delete=models.CASCADE)