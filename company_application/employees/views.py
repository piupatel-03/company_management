from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
import json

# Create your views here.


def employee_list(request):

    if request.method == "GET":
        employees = Employee.objects.all()

        data = []

        for employee in employees:
            data.append({
                "id": employee.id,
                "name": employee.name,
                "email": employee.email,
                "age": employee.age,
                "salary": str(employee.salary),
            })

        return JsonResponse(data, safe=False)

    if request.method == "POST":
        data = json.loads(request.body)

        employee = Employee.objects.create(
            name=data["name"],
            email=data["email"],
            age=data["age"],
            salary=data["salary"]
        )

        return JsonResponse({
            "id": employee.id,
            "name": employee.name,
            "email": employee.email,
            "age": employee.age,
            "salary": str(employee.salary),
        }, status=201)

    
