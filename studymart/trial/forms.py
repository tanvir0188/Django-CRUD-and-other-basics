from django import  forms
import email


class Teachers_reg(forms.Form):
    f_name = forms.CharField(label='Enter your firs name')
    l_name = forms.CharField(initial='StudyMart')
    email =  forms.EmailField()
    #if we want to have a fixed field then "email = forms.EmailField(initial = "something", disabled = True)"
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    checkBox = forms.CharField(widget=forms.CheckboxInput)
    def clean(self):
        cleaned_data = super().clean()
        right_pass = self.cleaned_data['password']
        wrong_pass = self.cleaned_data['re_password']
        if right_pass != wrong_pass:
            raise forms.ValidationError("Password does not match")


