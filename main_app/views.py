from django.shortcuts import render
from rest_framework import viewsets
from .models import Registration, ContactUs
from .serializers import RegistrationSerializer, ContactUsSerializer



class RegistrationAPI(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class ContactUsAPI(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    





