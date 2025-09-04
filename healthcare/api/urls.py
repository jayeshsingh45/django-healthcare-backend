from django.urls import path
from .authViews import RegisterView, LoginView
from .patientsViews import PatientCreateListView, PatientDetailView
from .mappingViews import MappingListCreateView, MappingView
from .doctorsViews import DoctorView

from rest_framework.routers import DefaultRouter

urlpatterns = [
    # Auth api
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),

    # Patients api
    path("patients/", PatientCreateListView.as_view(), name="patients-list-create"),
    path("patients/<int:pk>/", PatientDetailView.as_view(), name="patient-detail"),


    

    # Doctors api
    path("doctors/", DoctorView.as_view(), name="doctors-list-create"),
    path("doctors/<int:pk>/", DoctorView.as_view(), name="doctor-detail"),    

    # Mappings doctor to patients api
    path("mappings/", MappingListCreateView.as_view(), name="mapping-list-create"),
    path("mappings/<int:pk>/", MappingView.as_view(), name="mappings"),


]
