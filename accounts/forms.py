from django import forms
from django.contrib.auth.models import User
from . models import UserProfile

class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput(attrs={
       'placeholder' : 'Enter password',
       'class': 'form-control', 
    }))

    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={
       'placeholder' : 'Enter password',
       'class': 'form-control', 
    }))

    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']
        

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords does not match")
    
    def __init__(self,*args, **kwargs):
        super(RegistrationForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False,error_messages={'invalid':(" Images files only")},widget=forms.FileInput
        )
    
    class Meta:
        model = UserProfile
        fields = ['addrress_line_1','addrress_line_2','profile_picture','city','state','country']

    def __init__(self,*args, **kwargs):
        super(RegistrationForm,self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



