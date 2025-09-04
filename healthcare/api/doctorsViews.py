from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorView(APIView):
    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get(self, request, pk=None):
        """List all doctors or get details of a specific doctor"""
        if pk:
            doctor = get_object_or_404(Doctor, pk=pk)
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)
        doctors = Doctor.objects.all().order_by("-created_at")
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new doctor (auth required)"""
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Update doctor details (auth required)"""
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """Delete a doctor (auth required)"""
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor_name = doctor.name
        doctor.delete()
        return Response(
            {"message": f"Doctor '{doctor_name}' deleted successfully"},
            status=status.HTTP_200_OK
        )