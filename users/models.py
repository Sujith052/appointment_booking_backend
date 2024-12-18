from django.db import models
from guest.models import *

# Create your models here.
class appointmentbooking(models.Model):
    name=models.CharField(max_length=50)
    phone_number=models.BigIntegerField()
    date=models.DateField()
    selected_slote=models.ForeignKey(time_slot, on_delete=models.CASCADE, related_name='time_slot')
    user=models.ForeignKey(userdata, on_delete=models.CASCADE, related_name='user_id')
    booking_status=models.CharField(max_length=50)
    def __str__(self):
        return self.name