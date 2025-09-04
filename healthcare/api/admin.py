from django.contrib import admin
from .models import Patient, Doctor, PatientDoctorMap

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "created_by", "created_at")
    search_fields = ("name", "email")

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "specialization", "created_at")
    search_fields = ("name", "email", "specialization")

@admin.register(PatientDoctorMap)
class PatientDoctorMapAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "doctor", "assigned_by", "created_at")
    search_fields = ("patient__name", "doctor__name")
