from django.shortcuts import render
from Submitions.models import submition
from Submitions.serializer import submition_serializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from Auth.models import User
# Create your views here.



@api_view(['POST'])
def submit_answer(request):
    user = User.objects.filter(id=request.data['id']).first()
    print(user.id)
    serializer = submition_serializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"done"},status=status.HTTP_200_OK)
    else:
        print(serializer.errors)
        return Response({"message":"not done"})