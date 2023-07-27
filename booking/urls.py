# from django.urls import path


# urlpatterns = []

from django.urls import path
from . import views

urlpatterns = [
    # Add more URL patterns as needed
    #  path('bookSession/<int:id>', views.bookSession, name='bookSession'),
     path("appointment/",views.InsertAppointment, name="bookappointment"),
    #  path('deleteSession/<int:id>', views.cancelSession, name='deleteSession'),
     path('getdepartment/', views.getDepartment, name='getDepartments'),
]
