from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Registration, ContactUs


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration
        fields = ['email','first_name','last_name']

class ContactUsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['first_name','last_name','email','message']