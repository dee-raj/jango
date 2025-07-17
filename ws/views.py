from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            print("Fetching employee data for user:", request.user)
            employee = get_object_or_404(Employee, pk=request.user.id)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print("Error fetching employee data:", str(e))
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetAllEmployeesAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetEmployeeAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateEmployeeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            print("Creating employee with data:", request.data)
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Error during employee creation:", str(e))
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateEmployeeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            employee = get_object_or_404(Employee, pk=pk)
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Exception as e:
            print("Error during employee update:", str(e))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        password = request.data.get("password")
        if password:
            return Response({"error": "Use diifrent route to update password."}, status=status.HTTP_406_NOT_ACCEPTABLE)
        try:
            employee = get_object_or_404(Employee, pk=pk)
            serializer = EmployeeSerializer(
                employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Exception as e:
            print("Error during employee update:", str(e))
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateEmployeePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        password = request.data.get("password")
        if not password:
            return Response({"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST)

        from django.contrib.auth.hashers import make_password
        employee.password = make_password(password)
        employee.save()
        return Response({"detail": "Password updated successfully."})


class SoftDeleteEmployeeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.is_active = False
        employee.save()
        return Response({"detail": "Soft delete performed."}, status=status.HTTP_204_NO_CONTENT)


class HardDeleteEmployeeAPIView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response({"detail": "Employee deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
