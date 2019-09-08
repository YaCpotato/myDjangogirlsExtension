from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='tasks',null=True,blank=True)
    name = models.CharField(max_length=64)
    start = models.DateField()
    days = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)