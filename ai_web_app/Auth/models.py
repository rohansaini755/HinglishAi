from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("User must have email")

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        #extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)
        #extra_fields.setdefault("is_studet",False)
        #if extra_fields.get('is_staff') is not True:
         #   raise ValueError('superuser must have is_staff-true')
        
        #if extra_fields.get('is_superuser') is not True:
         #   raise ValueError('superuser must have is_superuser-true')

        return self.create_user(email,password,**extra_fields)


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email    = models.EmailField(max_length=100,unique=True)
    phone_number  = models.CharField(max_length=12,blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login  = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_staff      = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']

    objects = UserManager()

    def __str__(self):
        return self.email

    
    
# Create your models here.
