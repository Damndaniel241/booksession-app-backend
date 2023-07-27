from typing import Any
from django.contrib.auth.base_user import BaseUserManager

class customizeUser(BaseUserManager):

    def create_user(self,email,password, **kwargs):
        # return super().create(**kwargs)
        if not email:
            raise ValueError("please provide email address")
        

        email = self.normalize_email(email)

        user = self.model(email=email, **kwargs)

        user.set_password(password)

        user.save()

        return user 
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError(("Staff status must be True."))
        
        if kwargs.get("is_superuser") is not True:
            raise ValueError(("Superuser status must be True."))
        
        if kwargs.get("is_active") is not True:
            raise ValueError(("Superuser must be True."))
        
        user = self.create_user(email=email, password=password, **kwargs)

        return user
    
