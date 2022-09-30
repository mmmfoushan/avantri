from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=200)
    qualifications = models.CharField(max_length=200)
    experience = models.IntegerField()
    reporting_to = models.CharField(max_length=200)    
    class Meta:
        db_table="job"

