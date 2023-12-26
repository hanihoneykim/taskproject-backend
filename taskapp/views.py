from django.shortcuts import render
from django.views import View
from .models import Task, ChecklistItem


def index(request):
    context = {}
    return render(request, "pages/index.html", context)


class TaskListView(View):
    template_name = "pages/task_list.html"

    def get(self, request):
        tasks = Task.objects.all()
        context = {
            "tasks": tasks,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        context = {}
        return render(request, self.template_name, context)
