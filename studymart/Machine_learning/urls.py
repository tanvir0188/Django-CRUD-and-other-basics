
from django.urls import path
from . import views


urlpatterns = [

    path('', views.machine_learning, name='ml'),
    path('dl/', views.deep_learning, name ='dl'),

    path('about/', views.about, name='about'),
    path('teachers/', views.teachers_info, name = 'teacher_info'),
    path('teacher-reg/', views.teacher_form,  name = 'teacher_reg'),
    path('updateTeacher/<int:f_id>', views.update_teacher,  name = 'update_teacher'),
    path('deleteTeacher/<int:f_id>', views.delete_teacher,  name = 'delete_teacher'),

]