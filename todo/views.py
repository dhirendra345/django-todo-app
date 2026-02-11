from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Category, Task

class CategoryListView(ListView):
    model = Category
    template_name = 'todo/category_list.html'


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('category-list')


class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(
            category_id=self.kwargs['category_id']
        )


class TaskCreateView(CreateView):
    model = Task
    fields = ['category', 'title', 'description', 'completed']
    template_name = 'todo/task_form.html'

    def get_success_url(self):
        return reverse_lazy(
            'task-list',
            kwargs={'category_id': self.object.category.id}
        )
