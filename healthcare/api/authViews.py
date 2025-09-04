from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import RegisterSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # creating only access token (1 week is the expiry configured in settings.py)
        
        access = AccessToken.for_user(user)

        return Response({
            "message": "Registered successfully.",
            "user": {
                "id": user.id,
                "name": user.first_name,
                "email": user.email,
            },
            "token": str(access)  # return only access token
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"detail": "email and password required"}, status=400)

        # authenticate expects username; using email as username
        
        user = authenticate(username=email, password=password)
        if not user:
            return Response({"detail": "Invalid credentials"}, status=401)

        access = AccessToken.for_user(user)

        return Response({
            "message": "Login successful.",
            "user": {
                "id": user.id,
                "name": user.first_name,
                "email": user.email,
            },
            "token": str(access)  # only access token
        })
