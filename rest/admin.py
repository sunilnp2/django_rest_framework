from django.contrib import admin
from rest.models import Stud
# Register your models here.
class StudAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'city']
admin.site.register(Stud, StudAdmin)

