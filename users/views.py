from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from users.models import *
from guest.models import *
from guest.serializers import *
from users.serializers import *

# Create your views here.
@csrf_exempt
def appointmentsection(request):
    if request.method == "POST":
        try:
            # Retrieve the state name from the POST request
            name = request.POST.get('name')
            print(name)
            contactno = request.POST.get('contactno')
            date = request.POST.get('date')
            print(date)
            timeslot = request.POST.get('timeslot')
            booking_status = "Slote Booked"
            id=request.session['loginid']
            userid = userdata.objects.get(id=id)
            print(userid)
            sloteid=time_slot.objects.get(id=timeslot)

            # Create a new state object and save it to the database
            appoint_reg = appointmentbooking(name=name,phone_number=contactno,date=date,selected_slote=sloteid,user=userid,booking_status=booking_status)
            appoint_reg.save()

            return JsonResponse({'message': 'appointment successfully'}, status=201)

        except Exception as e:  # Handle any unexpected exceptions
            return JsonResponse({'error': str(e)}, status=500)
        
    elif request.method =="GET":
         appointment_times = appointment_time.objects.all() 
         serializer = appointment_timeSerializer(appointment_times, many=True)
         return JsonResponse(serializer.data, safe=False)
    
    # Return a 405 Method Not Allowed response for non-POST requests
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def getappointment_section(request,id):
    if request.method == "GET":
        print(id)
        time_slots = time_slot.objects.filter(appointment_time=id) 
        print(time_slots)
        serializer = timeSlotSerializer(time_slots, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # Return a 405 Method Not Allowed response for non-POST requests
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def getappointment_details(request):
    if request.method == "GET":
        userid = request.session['loginid']
        appointment_details = appointmentbooking.objects.select_related("selected_slote").filter(user=userid) 
        serializer = appointment_detailsSerializer(appointment_details, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # Return a 405 Method Not Allowed response for non-POST requests
    return JsonResponse({'error': 'Invalid request method'}, status=405)

