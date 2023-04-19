from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(
        User, 
        db_column="user",
        on_delete=models.CASCADE,
        default=1,
        null=True)
    title = models.CharField(max_length=250, blank = False)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add= True)
    

    class Meta:
        ordering = ['date_created']
    def __str__(self):
        return self. title