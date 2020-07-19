from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo import views

urlpatterns = [
    path('', views.TodoList.as_view()),
    path('<int:pk>/', views.TodoDetail.as_view())
]