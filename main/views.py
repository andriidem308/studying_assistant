from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DeleteView, ListView, View
from main.services.get_models import *
from main.models import Group, Student, Lecture, Task, Solution
from main.forms import GroupForm, StudentForm, LectureForm, TaskForm, SolutionForm

# Create your views here.


def index(request):
    return render(request, 'main/index.html', {'title': 'Домашня'})


def lectures(request):
    return render(request, 'main/lectures_list.html', {'title': 'Лекції'})


def tasks(request):
    return render(request, 'main/tasks.html', {'title': 'Задачі'})


def literature(request):
    return render(request, 'main/literature.html', {'title': 'Література'})


# ----- GROUPS -----


# def groups_all(request):
#     context = {'title': "Групи", "groups": group_all()}
#     return render(request, 'main/groups_all.html', context)


def group_update(request, group_id):
    """Update Posts."""
    err = ""
    pst = get_object_or_404(Group, pk=group_id)

    if request.method == "POST":
        form = GroupForm(instance=pst, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("group_list")
        else:
            err = "Не возможно обновить пост."
    else:
        form = GroupForm(instance=pst)
    context = {
        "form": form,
        "err": err
    }
    return render(request, "main/group_update.html", context=context)


def group_create(request):
    """Route Create Post."""
    errors = ''
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("group_list")
        else:
            errors = "Не возможно сохранить пост."
    else:
        form = GroupForm()
    context = {"form": form, "errors": errors}
    return render(request, "main/group_create.html", context=context)


def group_show(request, group_id):
    """Route to Post by ID."""
    group = group_find(group_id)
    all_students = students_by_group(group_id)
    context = {
        "title": group.name,
        "students": all_students
    }
    return render(request, "main/group_show.html", context)


class GroupsListView(ListView):
    """Show list of posts analogously."""

    def get_queryset(self):
        """Set queryset to listview."""
        queryset = group_all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        """Set context data for ListView."""
        context = super().get_context_data(*args, **kwargs)
        context["cnt"] = context['object_list'].count()
        context["title"] = "Всі групи"
        return context


class DeleteGroupView(DeleteView):
    """Delete posts."""

    model = Group
    template_name = "main/group_delete.html"
    success_url = reverse_lazy("group_list")


# ----- STUDENTS -----


def student_create(request):
    errors = ''
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("group_list")
        else:
            errors = "Невозможно сохранить пост."
    else:
        form = StudentForm()
    context = {"form": form, "errors": errors}
    return render(request, "main/student_create.html", context=context)


# ----- LECTURES -----


class LecturesGroupsListView(ListView):
    """Show list of posts analogously."""
    template_name = 'main/lectures_list.html'

    def get_queryset(self):
        """Set queryset to listview."""
        queryset = group_all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        """Set context data for ListView."""
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Всі лекції"

        return context


def lectures_show(request, group_id):
    group = group_find(group_id)
    group_lectures = lectures_by_group(group_id)

    context = {
        "title": group.name,
        "lectures": group_lectures
    }

    return render(request, "main/lectures_show.html", context)


def lecture_create(request):
    errors = ''
    if request.method == "POST":
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lectures_list")
        else:
            errors = "Невозможно сохранить пост."
    else:
        form = LectureForm()
    context = {"form": form, "errors": errors}
    return render(request, "main/lecture_create.html", context=context)


# ----- LECTURES -----


class TasksGroupsListView(ListView):
    """Show list of posts analogously."""
    template_name = 'main/tasks_list.html'

    def get_queryset(self):
        """Set queryset to listview."""
        queryset = group_all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        """Set context data for ListView."""
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Всі задачі"

        return context


def tasks_show(request, group_id):
    group = group_find(group_id)
    group_tasks = tasks_by_group(group_id)

    context = {
        "title": group.name,
        "tasks": group_tasks
    }
    return render(request, "main/tasks_show.html", context)


def task_create(request):
    errors = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks_list")
        else:
            errors = "Невозможно сохранить пост."
    else:
        form = TaskForm()
    context = {"form": form, "errors": errors}
    return render(request, "main/task_create.html", context=context)


def task_show(request, task_id):
    task = task_find(task_id)

    context = {
        "title": task.title,
        "description": task.description,
        "testfile": task.testfile,
    }

    return render(request, "main/task_show.html", context)
