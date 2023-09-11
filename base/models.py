from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    taskfield=models.CharField(max_length=200)
    completed=models.BooleanField(blank=True,null=True)
    class Meta:
        ordering=['id']
