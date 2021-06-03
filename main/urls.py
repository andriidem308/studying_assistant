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
    path('groups/', views.groups_all, name='groups_all'),


    path('lectures/', views.lectures, name='lectures'),
    path('tasks/', views.tasks, name='tasks'),
    path('literature/', views.literature, name='literature'),

    path('accounts/', include('django.contrib.auth.urls'), name='account'),


]

