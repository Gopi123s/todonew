from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    createdate=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        
        verbose_name = 'Task'
        verbose_name_plural = 'Task'
        ordering=['complete']

