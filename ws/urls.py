from django.urls import path
from .views import (
    GetAllEmployeesAPIView,
    EmployeeAPIView,
    GetEmployeeAPIView,
    CreateEmployeeAPIView,
    UpdateEmployeeAPIView,
    UpdateEmployeePasswordAPIView,
    SoftDeleteEmployeeAPIView,
    HardDeleteEmployeeAPIView,
)

urlpatterns = [
    path(
        "get-all/",
        GetAllEmployeesAPIView.as_view(),
        name="get-all-employees"
    ),

    path(
        "me/",
        EmployeeAPIView.as_view(),
        name="get-me"
    ),
    path(
        "get/<int:pk>/",
        GetEmployeeAPIView.as_view(),
        name="get-employee"
    ),

    path(
        "create/",
        CreateEmployeeAPIView.as_view(),
        name="create-employee"
    ),

    path(
        "update/<int:pk>/",
        UpdateEmployeeAPIView.as_view(),
        name="update-employee"
    ),

    path(
        "update-pass/<int:pk>/",
        UpdateEmployeePasswordAPIView.as_view(),
        name="update-password"
    ),

    path(
        "delete/<int:pk>/",
        SoftDeleteEmployeeAPIView.as_view(),
        name="soft-delete-employee"
    ),

    path(
        "delete-hard/<int:pk>/",
        HardDeleteEmployeeAPIView.as_view(),
        name="hard-delete-employee"
    ),
]
