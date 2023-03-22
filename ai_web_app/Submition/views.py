from django.shortcuts import render
from Submition.models import submition
from Submition.serializer import submition_serializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from Auth.models import User
import json
from Text.models import Text
#nltk.download('punkt')
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# Create your views here.


@api_view(['POST'])
def submission_list(request):
    user = User.objects.filter(username=request.data['username']).first()
    if user is None:
        return Response({"message":"user not exists"},status=status.HTTP_404_NOT_FOUND)
    
    submition_data = submition.objects.filter(username=request.data['username'],text_id=request.data['text_id'],flag=True).all().order_by('-submition_id')
    text = Text.objects.filter(text_id=request.data['text_id']).first()
    data = []
    for i in range(0,len(submition_data)):
        t = {}
        t['text_id'] = text.text_id
        t['text_name'] = text.name
        t['submition_id'] = submition_data[i].submition_id
        t['submit_answer'] = submition_data[i].answer
        t['suggestions'] = submition_data[i].suggestions
        t['accuracy'] = submition_data[i].accuracy
        t['answer_status'] = submition_data[i].answer_status
        # t['submition_date'] = submition_data[i].date
        t['level'] = text.level
        t['correct_answer'] = text.englishText
        data.append(t)
    return Response(json.dumps(data),status=status.HTTP_200_OK)

@api_view(['POST'])
def submit_answer(request):
    user = User.objects.filter(username=request.data['username']).first()
    if user is None:
        return Response({"message":"user not exists"},status=status.HTTP_404_NOT_FOUND)
    request.data['id'] = user.id
    q_id = request.data['text_id']
    e_text = request.data['answer']
    text = Text.objects.filter(text_id=q_id,flag1=True).first()
    if text == None:
        return Response({"message":"attack"},status=status.HTTP_404_NOT_FOUND)
    else:
        oe_text = text.englishText
        cosine = analyze(oe_text,e_text)

    score = cosine*100
    request.data['accuracy'] = score
    if score < 50:
        answer_status = "ok"
    elif score >= 50 and score < 75:
        answer_status = "good"
    else:
        answer_status = "best"
    request.data['answer_status'] = answer_status
    serializer = submition_serializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        # ans = []
        # data  = {}
        # data['text_id'] = text.text_id
        # data['name'] = text.name
        # data['level'] = text.level
        # data['sublevel'] = text.subLevel
        # data['correct_answer'] = text.englishText
        # data['accuracy'] = cosine*100
        # data['answer_status'] = answer_status
        # data['user_answer'] = e_text
        # data['suggestion'] = ""
        # ans.append(data)
        return Response({"message":"success"},status=status.HTTP_200_OK)
    else:
        print(serializer.errors)
        return Response({"message":"not done"})






def analyze(X,Y):
    # X = input("Enter first string: ").lower()
    # Y = input("Enter second string: ").lower()
    # X ="I love horror movies"
    # Y ="Lights out is a horror movie"

    # tokenization
    #nltk.download(‘all’)
    X_list = word_tokenize(X)
    Y_list = word_tokenize(Y)

    # sw contains the list of stopwords
    sw = stopwords.words('english')
    l1 =[];l2 =[]

    # remove stop words from the string
    X_set = {w for w in X_list if not w in sw}
    Y_set = {w for w in Y_list if not w in sw}
    # print(X_set)
    # print(Y_set)

    # form a set containing keywords of both strings
    rvector = X_set.union(Y_set)
    # print(rvector)
    for w in rvector:
        if w in X_set: l1.append(1) # create a vector
        else: l1.append(0)
        if w in Y_set: l2.append(1)
        else: l2.append(0)
    c = 0
    # print(l1)
    # print(l2)``
    # cosine formula
    for i in range(len(rvector)):
        c+= l1[i]*l2[i]
    cosine = c / float((sum(l1)*sum(l2))**0.5)
    # print("similarity: ", cosine)
    return cosine