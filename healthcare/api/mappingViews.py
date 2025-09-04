from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import PatientDoctorMap, Patient
from .serializers import PatientDoctorMapSerializer
from rest_framework.views import APIView

class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMapSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # any user can get any patients
        return PatientDoctorMap.objects.filter(patient__created_by=self.request.user).select_related("patient","doctor").order_by("-created_at")


class MappingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk=None):
        """List all mappings for a given patient"""
        patient = get_object_or_404(Patient, pk=pk)
        mappings = PatientDoctorMap.objects.filter(patient=patient).select_related("patient", "doctor").order_by("-created_at")
        serializer = PatientDoctorMapSerializer(mappings, many=True)
        return Response(serializer.data)

    def delete(self, request, pk=None):
        """Delete a specific mapping by id"""
        mapping = get_object_or_404(PatientDoctorMap, pk=pk)
        mapping.delete()
        return Response({"message": "Mapping deleted successfully"}, status=status.HTTP_200_OK)