from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMap

# ---------- AUTH ----------
class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "name", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 6},
            "email": {"required": True},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use.")
        return value

    def create(self, validated_data):
        name = validated_data.pop("name")
        email = validated_data.pop("email")
        password = validated_data.pop("password")
        # use email as username to simplify login
        user = User(username=email, email=email, first_name=name)
        user.set_password(password)
        user.save()
        return user

# ---------- DOMAIN ----------
class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Patient
        fields = ("id", "email", "name", "symptoms", "created_at", "created_by")
        read_only_fields = ("id", "created_at")

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ("id", "email", "name", "specialization", "created_at")
        read_only_fields = ("id", "created_at")

class PatientDoctorMapSerializer(serializers.ModelSerializer):
    patient_detail = PatientSerializer(source="patient", read_only=True)
    doctor_detail = DoctorSerializer(source="doctor", read_only=True)
    assigned_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PatientDoctorMap
        fields = ("id", "patient", "doctor", "assigned_by", "created_at",
                  "patient_detail", "doctor_detail")
        read_only_fields = ("id", "created_at")

    def validate(self, attrs):
        patient = attrs.get("patient")
        request = self.context["request"]
        # Ensure user can only map their own patients
        if patient.created_by != request.user:
            raise serializers.ValidationError("You can only map doctors for your own patients.")
        return attrs
