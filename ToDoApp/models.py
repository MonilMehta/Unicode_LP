from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tasks(models.Model):
    username = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    taskname = models.CharField(max_length=50,null=False)
    description = models.TextField(max_length=100,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    task_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.taskname
    

