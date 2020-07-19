from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'check', 'created_at', 'modified_at')