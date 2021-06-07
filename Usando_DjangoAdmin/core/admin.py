from django.contrib import admin
from django.contrib.auth.models import Group, User
from core.models import Empregado

# Register your models here.
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Empregado)