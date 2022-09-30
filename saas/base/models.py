from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    name = models.CharField(max_length=200)
    qualifications = models.CharField(max_length=200)
    experience = models.IntegerField()
    reporting_to = models.CharField(max_length=200)    
    class Meta:
        db_table="job"

class WorkHistory(models.Model):
    position = models.CharField(max_length=200)
    workplace = models.CharField(max_length=200)
    start = models.DateField()
    end = models.DateField()
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)    
    class Meta:
        db_table="workhistory"

