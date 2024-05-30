from django import forms
from .models import Registration,Blogs

class SignupForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['first_name','last_name','email','password','phone_number','confirm_password']
        
                


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title','author','content', 'slug', 'status']




        