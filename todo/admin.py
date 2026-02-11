from django.contrib import admin
from .models import Category, Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [TaskInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Task)
