from .models import Todo
from rest_framework import serializers
from usermanagement.models import TodoUser
from datetime import datetime

class TodoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200, required=True)
    description = serializers.CharField(max_length=500, required=False)
    check = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(read_only=True)
    modified_at = serializers.DateTimeField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(queryset=TodoUser.objects.all())

    def create(self, validated_data, *args, **kwargs):
        return Todo.objects.create(modified_at=datetime.now(), **validated_data)

    def update(self, instance, validated_data):
        instance.title = validatd_data.get('title', instance.title)
        instance.description = validatd_data.get('description', instance.description)
        instance.check = validated_data.get('check', instance.check)
        instance.modified_at = datetime.now()
        instance.save()
        return instance

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'check', 'created_at', 'modified_at', 'owner')