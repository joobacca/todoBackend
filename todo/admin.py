from django.contrib import admin
from .models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    # fields = ('title', 'description', 'check')
    exclude = ['created_at']
        

admin.site.register(Todo, TodoAdmin)