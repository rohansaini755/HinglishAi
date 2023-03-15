from django.shortcuts import render
from rest_framework.decorators import api_view 
from .models import User
from django.http import HttpResponse
from rest_framework import status
import json
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def signup(request):
    first_name = request.data['first_name']
    print(first_name)
    last_name = request.data['last_name']
    if len(first_name) < 3 or len(last_name) < 3:
        res = {'message':' Max length of First name and Last name should be greater than 3.'}
        res = json.dumps(res)
        res = {'response':res}
        return Response(res,status=status.HTTP_403_FORBIDDEN)
    email     = request.data['email']

    user = User.objects.filter(email = email).first()
    if user is not None:
        res = {'message':'User with email is already exists.'}
        res = json.dumps(res)
        res = {'response':res}
        return Response(res,status=status.HTTP_208_ALREADY_REPORTED)


    phone_number = request.data['phone_number']

    username = first_name[0:3] + last_name[0:3]
    password = username
    user = User.objects.create_user(email,password)
    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    user.phone_number = phone_number
    user.save()
    res = {'message':'created successfully'}
    res = json.dumps(res)
    res = {'response':res}

    return Response(res,status=status.HTTP_200_OK)


@api_view(['POST'])
def signin(request):
    email = request.data['email']
    user = User.objects.filter(email=email).first()
    if user is None:
        return Response({"message":"User not found"},status=status.HTTP_404_NOT_FOUND)

    if not user.is_active:
        return Response({"message":"User is Blocked"},status=status.HTTP_401_UNAUTHORIZED) 

    password = request.data['password']

    if not user.check_password(password):
        return Response({"message":"Incorrect Password"},status=status.HTTP_401_UNAUTHORIZED)

    data = {}
    data['message'] = "successfully login"
    data['username'] = user.first_name
    return Response(data,status=status.HTTP_200_OK)

def signout(request):
    pass