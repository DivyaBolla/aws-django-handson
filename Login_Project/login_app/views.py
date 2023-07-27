from django.shortcuts import render
from django.http import HttpResponse
from . models import User
from django.http import HttpResponse, JsonResponse
from . models import User
from . serializers import UserSerializer
from rest_framework.parsers import JSONParser
# Create your views here.

def Homepage(request):
    return render(request, 'login_app\homepage.html')

def Index(request):
    #all_objects = User.objects.all()
    #print (all_objects)
    return render(request, 'login_app\index.html')

def alldetails(request):
    try:
        all_data = User.objects.all()
    except:
        return HttpResponse('Sorry..! No data found', status = 404)
    if request.method == 'GET':
        user = UserSerializer(all_data, many = True)
        return JsonResponse(user.data, safe = False)

    elif request.method == 'POST' :
        input_data = JSONParser().parse(request)
        serializer = UserSerializer(data = input_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        else:
             return HttpResponse('Sorry..! No data found', status = 404)