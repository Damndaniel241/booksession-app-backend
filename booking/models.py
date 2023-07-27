from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title



class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    reference = models.CharField(max_length=50, null=True,blank=True)
    chosen_time = models.DateTimeField()
    dpt = models.ForeignKey(Department,on_delete=models.RESTRICT)   


    def __str__(self):
        return f"{self.name}'s appointment"
    
   







# assignment

# create a logic (views.py) to check if person provides name, date, chosen time






# cascade =delete appointment altogether models.CASCADE

   #restrict  = appointment won't delete  models.DELETE