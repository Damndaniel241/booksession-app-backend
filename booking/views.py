from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers,status
from .models import Appointment,Department
from account.models import User
from phonenumber_field.serializerfields import PhoneNumberField


# Create your views here.


class dptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
    
@api_view(['GET'])
def getDepartment(request):
    dpt = Department.objects.all()
    serializerdata = dptSerializer(dpt,many=True)

    return Response(serializerdata.data)


# class DepartmentSerializer(serializers.ModelSerializer):
#     dpt_id = serializers.IntegerField(required=True)

#     class Meta:
#         model = Department
#         fields = '__all__'


# class PhoneNumberSerializer(serializers.Serializer):
#     phone = PhoneNumberField(region="CA")
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

@api_view(['POST'])
def InsertAppointment(request):
    serializerdata = AppointmentSerializer(data = request.data)

    if serializerdata.is_valid():
        serializerdata.save()
        return Response("success")

    else:
        return Response(serializerdata.errors)



class bookingSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    chosen_time = serializers.DateTimeField()
    dpt_id = serializers.IntegerField(required=True)
    # phone = serializers.CharField()
    # phone = PhoneNumberSerializer()
    # email = serializers.EmailField(read_only=True)

    # date = serializers.DateTimeField(read_only=True)
    # dpt = DepartmentSerializer.dpt_id
    # dpt = serializers.CharField()


    class Meta:
        model = Appointment
        fields = ['name','chosen_time','dpt_id']

    # def validate(self, data):
    #     check = User.objects.filter(email = data['email']).first()

    #     if check is not None:
    #         raise serializers.ValidationError({"email":"email already exists"})
        
    
    #     return data


   


@api_view(['POST'])
def bookSession(request,id):
    try:
        user = User.objects.filter(id= id).first()

        if user is None:
            return Response("No user in database")  

        



        else:
        #     request_data = request.data.copy()

        # # Add the user's email to the data before passing it to the serializer
        #     request_data['email'] = user.email



            serializerdata = bookingSerializer(data=request.data)
            if serializerdata.is_valid():
                serializerdata.save()
                return Response("Appointment booked")
            else:
                return Response(serializerdata.errors)
    
    except BaseException as e:
        return Response(str(e))
    

@api_view(['DELETE'])
def cancelSession(request,id):
    try:
        booking_session = Appointment.objects.get(id=id)
        booking_session.delete()
        return Response("Appointment cancelled")
    except Appointment.DoesNotExist:
        return Response("Appointment not found")
    except BaseException as e:
            return Response(str(e))