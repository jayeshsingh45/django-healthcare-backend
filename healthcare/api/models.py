from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Patient(TimeStampedModel):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    symptoms = models.TextField(blank=True)
    # any user can get any patients
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patients")

    def __str__(self):
        return f"{self.name} ({self.email})"

class Doctor(TimeStampedModel):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"

class PatientDoctorMap(TimeStampedModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="mappings")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="mappings")
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assignments")

    class Meta:
        unique_together = ("patient", "doctor")

    def __str__(self):
        return f"{self.patient} -> {self.doctor}"
