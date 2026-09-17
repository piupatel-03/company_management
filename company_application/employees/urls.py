from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (EmployeeListCreateView, EmployeeDetailView,
                    DepartmentListCreateView, DepartmentDetailView)

urlpatterns = [
    path("employees/", EmployeeListCreateView.as_view()),
    path("employees/<int:pk>/", EmployeeDetailView.as_view()),
    path("departments/", DepartmentListCreateView.as_view()),
    path("departments/<int:pk>/", DepartmentDetailView.as_view()),

]
   