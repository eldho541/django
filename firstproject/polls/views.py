from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee
from .serializers import EmployeeSerializers


class employeelist(APIView):
    print(".....................................................")
    def get(self,request):
        employee1 =Employee.objects.all()
        # print(employee1)
        serializer=EmployeeSerializers(employee1,many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self):
        pass

# def index(response):
    
#     return HttpResponse("Hello you are at poll")


# Create your views here.
