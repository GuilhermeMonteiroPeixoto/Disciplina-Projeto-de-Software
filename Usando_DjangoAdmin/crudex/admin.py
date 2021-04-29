from django.contrib import admin
from django.contrib.auth.models import Group
from crudex.models import Empregado

admin.site.site_header = 'Folha de Pagamento'
admin.site.register(Empregado)
admin.site.unregister(Group)