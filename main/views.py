from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DeleteView, ListView, View
from main.services.group_service import group_all, group_find
from main.models import Group
from main.forms import GroupForm

# Create your views here.


def index(request):
    return render(request, 'main/index.html', {'title': 'Домашня'})


def lectures(request):
    return render(request, 'main/lectures.html', {'title': 'Лекції'})


def tasks(request):
    return render(request, 'main/tasks.html', {'title': 'Задачі'})


def literature(request):
    return render(request, 'main/literature.html', {'title': 'Література'})


def groups_all(request):
    context = {'title': "Групи", "groups": group_all()}
    return render(request, 'main/groups_all.html', context)


def group_update(request, group_id):
    """Update Posts."""
    err = ""
    pst = get_object_or_404(Group, pk=group_id)

    if request.method == "POST":
        form = GroupForm(instance=pst, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("groups_all")
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
            return redirect("groups_all")
        else:
            errors = "Не возможно сохранить пост."
    else:
        form = GroupForm()
    context = {"form": form, "errors": errors}
    return render(request, "main/group_create.html", context=context)


def group_show(request, group_id):
    """Route to Post by ID."""
    group = group_find(group_id)
    return render(request, "main/group_show.html", {"title": group.name})


class GroupsListView(ListView):
    """Show list of posts analogously."""

    def get_queryset(self):
        """Set queryset to listview."""
        queryset = Group.objects.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        """Set context data for ListView."""
        context = super().get_context_data(*args, **kwargs)
        context["cnt"] = context['object_list'].count()
        context["title"] = "Всі групи"
        return context


class DeletePostView(DeleteView):
    """Delete posts."""

    model = Group
    template_name = "main/group_delete.html"
    success_url = reverse_lazy("group_list")
