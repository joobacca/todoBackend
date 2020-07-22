from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200, required=True)
    description = serializers.CharField(max_length=500, required=False)
    check = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(read_only=True)
    modified_at = serializers.DateTimeField()
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'check', 'created_at', 'modified_at', 'user')