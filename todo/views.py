from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
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

    @action(detail=False, methods=['post'], name='Create Todo', url_path='create', permission_classes=[permissions.IsAuthenticated])
    def create_todo(self, request):
        data = request.data.copy()
        user = request.user
        print(self.request.user)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response({"message": "Todo Created"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

    @action(detail=False, methods=['get'], name='List my Todos', url_path='my-todos', permission_classes=[permissions.IsAuthenticated])
    def get_my_todos(self, request):
        user = request.user
        print(user)
        serializer = TodoSerializer(Todo.objects.filter(owner=user.id), many=True)
        
        return Response(serializer.data)

    # def get_permissions(self):
    #     if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
    #         permission_classes = [permissions.IsAuthenticated, ]
    #     else:
    #         permission_classes = [permissions.AllowAny]
    #     return [permission() for permission in permission_classes]

# @api_view(['GET', 'POST'])
# def todos(request):
#     if request.method == 'POST':
#         data = request.data
#         serializer = TodoSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response({"message": "Todo Created"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)
            