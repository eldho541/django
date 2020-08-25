from rest_framework import serializers
from polls.models import Employee

class EmployeeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields =("firstname","lastname")

 