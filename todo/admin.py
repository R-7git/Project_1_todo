from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')
    search_fields = ('task',)
    list_filter = ('is_completed',)

admin.site.register(Task, TaskAdmin)

