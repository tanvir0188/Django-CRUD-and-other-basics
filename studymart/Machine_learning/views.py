

from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render

from .models import Teachers
from .forms import TeacherForm

def machine_learning(request):
    name = 'arnob tanvir'
    students = ['arnob', 'ohi', 'tahsin']
    class_name = 'CSE289'
    is_lower = name.islower()
    page = {'Page_name': 'machine learning', 'name':name, 'c_name':class_name, 'is_lower':is_lower,
                'teachers':students, 'number_of_students':len(students)
            }
    return render(request, 'machineLearning/machine_learning.html', context = page)

def deep_learning(request):
    page = {'Page_name': 'deep learning'}
    return render(request,'machineLearning/deep_learning.html', context = page)


def about(request):
    page = {'Page_name': 'about'}
    return render(request,'machineLearning/about.html', context = page)

def teachers_info(request):
    teach = Teachers.objects.all()
    teach_dictionary = {'teacher_table':teach, 'Page_name': 'Teachers'}
    return render(request,'machineLearning/teacher.html', context=teach_dictionary)

def teacher_form(request):
    form =  TeacherForm()
    if  request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Teacher added successfully")
            return redirect("teacher_info")
        else:
            messages.error(request,"Teacher not added")
    context = {'form': form}
    return render(request, "machineLearning/teacherForm.html", context)

def update_teacher(request, f_id):
    teacher = Teachers.objects.get(id=f_id)
    form = TeacherForm(instance=teacher)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher updated")
            return redirect("teacher_info")
    
    context = {'form': form}
    return render(request, "machineLearning/teacherForm.html", context)

def delete_teacher(request, f_id):
    teacher = Teachers.objects.get(id=f_id)
    if request.method =="POST":
        teacher.delete()
        return redirect("teacher_info")
    
    return render(request, "machineLearning/confirmation.html", {"teacher": teacher})
    




