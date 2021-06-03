"""Project urls."""
# from django.contrib import admin
# from django.conf.urls import url
from django.urls import path, include
from django.views.decorators import cache
from django.views.generic import TemplateView

from . import views
urlpatterns = [
    path('', views.index, name='homepage'),
    # path('', TemplateView.as_view(template_name='main/index.html'), name='homepage'),

    path('groups/new', views.group_create, name='group_create'),
    path('groups/<int:group_id>/', views.group_show, name='group_show'),
    path('groups/update/<int:post_id>/', views.group_update, name='group_update'),
    path('groups/list/', views.GroupsListView.as_view(), name='group_list'),

    path('groups/<int:group_id>/lectures/', views.lectures_show, name='lectures_show'),
    path('groups/<int:group_id>/tasks', views.tasks_show, name='tasks_show'),

    path('students/new', views.student_create, name='student_create'),
    # path('students/<int:group_id>/<int:student_id>', views.student_show, name='student_show'),

    path('lectures/list', views.LecturesGroupsListView.as_view(), name='lectures_list'),
    path('lectures/new', views.lecture_create, name='lecture_create'),


    path('tasks/list', views.TasksGroupsListView.as_view(), name='tasks_list'),
    path('tasks/new', views.task_create, name='task_create'),
    path('tasks/<int:task_id>', views.task_show, name='task_show'),

    # path('tasks/<int:task_id>/solution', views.new_solution, name='new_solution'),
    #
    # path('solutions/<int:solution_id>/result', views.solution_result, name='solution_result'),

    # path('literature/', views.literature, name='literature'),

    path('accounts/', include('django.contrib.auth.urls'), name='account'),
]


