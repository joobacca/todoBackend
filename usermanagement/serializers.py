from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class BaseUserSerializer(RegisterSerializer):
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)

    def get_cleaned_data(self):
        super(BaseUserSerializer, self).get_cleaned_data()

        return {
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'username': self.validated_data.get('username', ''),
        }

    
#https://dev.to/callmetarush/the-django-rest-custom-user-model-and-authentication-5go9