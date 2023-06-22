from django.db import models

# Create your models here.
class LiveChat(models.Model):
    chat_details = models.TextField()
    associated_with_user = models.ForeignKey('User', on_delete=models.CASCADE)
