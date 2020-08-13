from django.db import models
from django.conf import settings

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    check = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title 