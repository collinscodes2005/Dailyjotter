from django import forms
from django.forms import TextInput
from django.forms.models import ModelForm
from .models import Author,Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'image', 'content', ]
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Enter title'}),
            'excerpt': TextInput(attrs={'placeholder': 'Enter excerpt'}),
        }

'''Login form '''
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


'''Sign up form '''
class SignUpForm(forms.Form):
    first_name = forms.CharField(label="Firstname", max_length=200)
    surname = forms.CharField(label = "Lastname", max_length=120)
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    