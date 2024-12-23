from django.db import models

# Create your models here.
class userdata(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contactno=models.BigIntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class appointment_time(models.Model):
    appointment_time=models.CharField(max_length=50)
    def __str__(self):
        return self.appointment_time

class time_slot(models.Model):
    timeslote=models.CharField(max_length=50)
    appointment_time=models.ForeignKey(appointment_time, on_delete=models.CASCADE, related_name='appointments')
    def __str__(self):
        return self.timeslote
    

