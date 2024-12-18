import datetime
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from guest.models import *

# Create your views here.
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contactno')
        username = request.POST.get('username')
        password = request.POST.get('password')
                
        userdata.objects.create(
            name=name,
            email=email,
            contactno=contact,
            username=username,
            password=password
            )
                
        return JsonResponse({'message': 'registered successfully!'}, status=201)
    
@csrf_exempt
def signin(request):
    if request.method == 'POST':
        # Parse the login data
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        # Check if login exists
        try:
            loginobj = userdata.objects.get(username=username)
            print(username)
            
            # Validate password (if hashed, use check_password)
            if loginobj.password == password:  # Replace with `check_password(password, loginobj.password)` if hashed
                request.session['username'] = loginobj.username
                print(loginobj.id)
                request.session['loginid'] = loginobj.id

                # Return role-based response
                return JsonResponse({'status': 'success','message': 'User login successful','role': 'USER','username': loginobj.username,'loginid': loginobj.id,
                }, status=200)

                # If the account is inactive
            return JsonResponse({'status': 'error','message': 'Account is inactive',}, status=403)
        except userdata.DoesNotExist:
            # If the username does not exist
            return JsonResponse({'status': 'error','message': 'Invalid username',}, status=404)

    # If the request method is not POST
    return JsonResponse({'status': 'error','message': 'Invalid request method',}, status=405)