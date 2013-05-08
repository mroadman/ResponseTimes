from django.db import models
from datetime import datetime

# Create your models here.
class Response(models.Model):
    inci_no = models.CharField(max_length=20, primary_key=True)
    dispatch = models.DateTimeField(default=datetime.now(),blank=True)
    alarm = models.DateTimeField(default=datetime.now(),blank=True)
    arrival = models.DateTimeField(default=datetime.now(),blank=True)
    dispatch_time = models.FloatField()
    rolldrive_time = models.FloatField()
    response_time = models.FloatField()
    inci_type = models.CharField(max_length=20, blank=True, null=True)
    descript = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=350, blank=True, null=True)
    station = models.CharField(max_length=20, blank=True, null=True)
    year = models.CharField(max_length=20, blank=True, null=True)
    month = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
    	db_table = 'ALLCALLS'

    def __unicode__(self):
    	return self.inci_no