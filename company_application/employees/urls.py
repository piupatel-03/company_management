from django.urls import path
from .views import (employee_list, 
        employee_detail,department_list,department_detail)

urlpatterns = [
    path("employees/", employee_list),
    path("employees/<int:pk>/", employee_detail), 
    path ("departments/", department_list),  
    path("departments/<int:pk>/", department_detail),
]