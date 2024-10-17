
from django.urls import path

from . import views

urlpatterns = [
    path('contact/', views.contact,  name='contact'),
    path('forms/',views.show_form_data,  name='forms'),
    path('class/',views.Contact.as_view(),  name='class'),



]