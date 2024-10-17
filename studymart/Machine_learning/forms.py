from cProfile import label
from dataclasses import field
from tkinter.ttk import Widget
from django import forms
from .models import Teachers

class  TeacherForm(forms.ModelForm):
    class Meta:
        model =  Teachers
        fields = '__all__'
        label = {
            'tid': 'Teacher_id',
            'tname': 'Teacher_name',
            'tmails': 'Teacher_email'
        }

        Widgets = {
            'tid':  forms.TextInput(attrs={'placeholder': 'Enter the id'}),
            'tname':  forms.TextInput(attrs={'placeholder': 'Enter the name'}),
            'tmails':   forms.EmailInput(attrs={'placeholder': 'Enter the email'})
        }
        
    

