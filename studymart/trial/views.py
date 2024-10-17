from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from . forms import Teachers_reg

# Create your views here.

def contact(request):
    page = {'Page_name':'Contact'}
    return render(request,'Contact/Contact.html', context = page)




def show_form_data(request):
    #validation

    if request.method == 'POST':
        fb=Teachers_reg(request.POST)
        print(fb)
        print("post statement")
        print(fb.cleaned_data)#gives you the data only, if you don't use it then you will get html tags

    else:
        fb=Teachers_reg()
        print("get statement")

    return render(request, 'forms/forms.html',  {'form': fb})

class Contact(View):
    def get(self, request):
        page = {'Page_name':'Class'}
        return render(request, 'Contact/class.html', context = page)
