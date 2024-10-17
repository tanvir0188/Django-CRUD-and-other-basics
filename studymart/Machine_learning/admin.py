from django.contrib import admin
from Machine_learning.models import Teachers
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','tid', 'tname', 'tmails')

admin.site.register(Teachers, TeacherAdmin)