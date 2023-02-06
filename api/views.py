from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework import authentication, permissions

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import api_view


# Class based

class List_Employee(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class Details_Employee(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, pk , format=None):
        id = Employee.objects.get(pk=pk)
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data,instance=id)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk , format=None):
        id = Employee.objects.get(pk=pk)
        id.delete()
        return JsonResponse('Data deleted successfully', status=200,safe=False)


# Function Based
# @api_view(['POST','GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
# @csrf_exempt
# def List_Employee(request):
#     if request.method == 'GET':
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = EmployeeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @api_view(['PUT','DELETE'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
# @csrf_exempt
# def Details_Employee(request,pk):
#     if request.method == 'PUT':
#         id = Employee.objects.get(pk=pk)
#         data = JSONParser().parse(request)
#         serializer = EmployeeSerializer(data=data,instance=id)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     if request.method == 'DELETE':
#         data = Employee.objects.get(pk=pk)
#         data.delete()
#         return JsonResponse('Data deleted successfully', status=200,safe=False)
