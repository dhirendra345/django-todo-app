from django.urls import path
from .views import *

urlpatterns = [
    path('', ListListView.as_view(), name='list-list'),
    path('list/add/', ListCreateView.as_view(), name='list-create'),
    path('list/delete/<int:pk>/', ListDeleteView.as_view(), name='list-delete'),

    path('tasks/<int:list_id>/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:list_id>/add/', TaskCreateView.as_view(), name='task-create'),
    path('list/update/<int:pk>/', ListUpdateView.as_view(), name='list-update'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),

    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]
