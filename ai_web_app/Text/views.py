from django.shortcuts import render
from rest_framework.decorators import api_view 
from .models import Text
from rest_framework.response import Response
import json
from .serializer import textSerializer
from rest_framework import status


@api_view(['POST'])
def add_text(request):
    serializer = textSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"message":"done"},status=status.HTTP_200_OK)

@api_view(['POST'])
def get_text_v1(request):
    pass


@api_view(['GET'])
def get_text(request):
    text1 = Text.objects.all()
    # data = {}
    text = []
    for it in text1:
        data = {}    
        data['name'] = it.name
        edata = it.hindiText
        hex_representation = edata.encode("utf-8").hex()
        edata = hex_representation
        data['hindiText'] = edata
        data['englishText'] = it.englishText
        hdata = it.hintString
        hdata = hdata.encode("utf-8").hex()
        data['hintString']  = hdata
        text.append(data)

    res = Response(json.dumps(text))
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res

@api_view(['POSt'])
def update_text(request):
    id = request.data['id']
    text = Text.objects.filter(text_id = id).first()
    serializer = textSerializer(text,data = request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        res = json.dumps({'message':'data updated','error':False})
        res = {"response":res}
        return Response(res,status=status.HTTP_200_OK)    
    return Response(serializer.errors)


@api_view(['POST'])
def get_demo_text(request):
    text1 = Text.objects.filter(text_id = 3).all()
    # data = {}
    text = []
    for it in text1:
        data = {}
        data['name'] = it.name
        edata = it.hindiText
        hex_representation = edata.encode("utf-8").hex()
        edata = hex_representation
        data['hindiText'] = edata
        data['englishText'] = it.englishText
        hdata = it.hintString
        hdata = hdata.encode("utf-8").hex()
        data['hintString']  = hdata
        text.append(data)

    res = Response(json.dumps(text))
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res

@api_view(['POST'])
def text(request):
    id = request.data['id']
    text = Text.objects.filter(text_id=id).first()
    if text != None:
        data = {}
        data['name'] = text.name
        edata = text.hindiText
        hex_representation = edata.encode("utf-8").hex()
        edata = hex_representation
        data['hindiText'] = edata
        hdata = text.hintString
        hdata = hdata.encode("utf-8").hex()
        data['hintString']  = hdata
        res = Response(json.dumps(data),status=status.HTTP_200_OK)
        res.headers["Access-Control-Allow-Origin"] = "*"
        return res
    else:
        return Response({"message":"not found"},status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def submit_analysis(request):
    q_id = request.data['id']
    e_text = request.data['text']
    text = Text.objects.filter(text_id=q_id).first()
    if text == None:
        return Response({"message":"attack"},status=status.HTTP_404_NOT_FOUND)
    else:
        oe_text = text.englishText
        return Response({"message":"successfully submitted"})
