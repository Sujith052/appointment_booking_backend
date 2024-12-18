from rest_framework import serializers
from guest.models import *

class appointment_timeSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment_time
        fields = '__all__'
        
class timeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = time_slot
        fields = '__all__'