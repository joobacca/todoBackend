from __future__ import unicode_literals
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
import requests

# Create your views here.

class EmailConfirmationView(APIView):
    permission_classes = [permissions.AllowAny,]
    def get(self, request, format=None, *args, **kwargs):
        responseData = requests.post(request.scheme + '://' + request.get_host() + reverse('rest_verify_email'), self.kwargs)
        return Response(responseData.json())