from django.db import models
from manager.models import Manager
from salesperson.models import Salesperson

# Create your models here.
class Lead(models.Model):
    lead_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    comment = models.TextField()
    lead_status = models.CharField(max_length=50)
    assigned_to = models.ForeignKey(Salesperson, on_delete=models.CASCADE, related_name='leads_assigned')
    qualified_by = models.ForeignKey(Salesperson, on_delete=models.CASCADE, related_name='leads_qualified')
    imported_by = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='leads_imported')
    belongs_to = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='leads')
