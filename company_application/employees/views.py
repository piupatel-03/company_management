from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response


# Create your views here.

@api_view(["GET", "POST"])
def employee_list(request):

    if request.method == "GET":
        employees = Employee.objects.all()

        serializer = EmployeeSerializer(employees, many=True)


        return Response(serializer.data)

        

    if request.method == "POST":
       serializer = EmployeeSerializer(data=request.data)

       if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)

       return Response(serializer.errors, status=400)

    
@api_view(["GET", "PUT", "PATCH", "DELETE"])
def employee_detail(request, pk):

    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNoteExist:
        return Response(
            {"error": "Employee not found"},
            ststus=404
        )

    if  request.method == "GET":
        serializer = EmployeeSerializer(employee)

        return Response(serializer.data)

    if request.method == "PUT":
        serializer = EmployeeSerializer(
            employee, data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == "PATCH":
        serializer = EmployeeSerializer(
            employee,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors,status=400)

    if request.method == "DELETE":
        employee.delete()

        return Response(status=204)




    
