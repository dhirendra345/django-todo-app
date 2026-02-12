from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import List, Task


class ListListView(ListView):
    model = List
    template_name = 'todo/list_list.html'


class ListCreateView(CreateView):
    model = List
    fields = ['name']
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('list-list')


class ListDeleteView(DeleteView):
    model = List
    template_name = 'todo/confirm_delete.html'
    success_url = reverse_lazy('list-list')


class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(
            list_id=self.kwargs['list_id']
        )


class TaskCreateView(CreateView):
    model = Task
    fields = ['list', 'title', 'description', 'completed']
    template_name = 'todo/task_form.html'

    def get_success_url(self):
        return reverse_lazy(
            'task-list',
            kwargs={'list_id': self.object.list.id}
        )


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(
            'task-list',
            kwargs={'list_id': self.object.list.id}
        )
