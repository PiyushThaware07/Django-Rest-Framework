from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


# Create your views here.
# django rest framework allow to create a class based views
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # custom apis --> get all employee within a company ~> companies/{companyId}/employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None): # pk is company id
        try:
            company =  Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company_detail=company)
            # serializer this emps object
            emps_serializer = EmployeeSerializer(emps,many=True,context={"request":request})
            return Response(emps_serializer.data)
        except Exception as e:
            return Response({
                "status" : "failed",
                "message":str(e)
            })




class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer