from django.contrib import admin
from .models import User, Task

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile')
    search_fields = ('name', 'email', 'mobile')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'created_at', 'completed_at')
    search_fields = ('name', 'status')
    list_filter = ('status', 'created_at')
    filter_horizontal = ('assigned_users',)  # For ManyToMany fields
