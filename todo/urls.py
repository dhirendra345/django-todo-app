from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('category/add/', CategoryCreateView.as_view(), name='category-create'),
    path('tasks/<int:category_id>/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:category_id>/add/', TaskCreateView.as_view(), name='task-create'),
]
