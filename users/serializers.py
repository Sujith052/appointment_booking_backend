from rest_framework import serializers
from users.models import *
from guest.serializers import *

class appointment_detailsSerializer(serializers.ModelSerializer):
    time_slot_details = timeSlotSerializer(source='time_slot', read_only=True)  
    class Meta:
        model = appointmentbooking
        fields = '__all__'