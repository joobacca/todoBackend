from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from .models import Todo
from .serializers import TodoSerializer
from usermanagement.permissions import IsOwnerOrReadOnly

class TodoViewSet(mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['post'], name='Create Todo', url_path='create', permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def create_todo(self, request):
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "Todo Created"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    
    def retrieve(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]