from rest_framework import serializers
from .models import *

# Create Serializers Here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField() # by  default it is hidden but to show you can use this
    class Meta:
        model = Company
        fields = "__all__" # if you want to inculde all the fields of company model

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"