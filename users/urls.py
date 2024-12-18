from django.urls import path
from users import views
 
urlpatterns = [
    path('appointmentsection', views.appointmentsection, name="appointmentsection"),
    path('getappointment_section/<id>', views.getappointment_section, name="getappointment_section"),
    path('getappointment_details', views.getappointment_details, name="getappointment_details"),
    
]