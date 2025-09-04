from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Patient
from .serializers import PatientSerializer




class PatientCreateListView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
         # return ALL patients regardless of who created them
        return Patient.objects.all().order_by("-created_at")
        # return Patient.objects.filter(created_by=self.request.user).order_by("-created_at")


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]  # any logged-in user can access
    queryset = Patient.objects.all()

    def delete(self, request, *args, **kwargs):
        patient = self.get_object()
        patient_name = patient.name
        self.perform_destroy(patient)
        return Response(
            {"message": f"Patient '{patient_name}' deleted successfully"},
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        patient = self.get_object()
        response = super().update(request, *args, **kwargs)
        return Response(
            {
                "message": f"Patient '{patient.name}' updated successfully",
                "data": response.data
            },
            status=status.HTTP_200_OK
        )