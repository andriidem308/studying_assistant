from account.models import User
from django.contrib import admin
from main.models import Group, Material, Student



# Register your models here.
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Material)
admin.site.register(User)