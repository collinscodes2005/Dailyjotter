from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from .models import Author,Post
from .forms import PostForm, LoginForm, SignUpForm


# Create your views here.
def indexPage(request):
       return render(request, "Dailyjotter/base.html")


def loginView(request):
   form = LoginForm() 
   if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():

            usernames = Author.objects.values_list('user_name', flat=True)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(user_name=username)

            if Author.objects.filter(user_name=username).exists() and Author.objects.filter(password=password).exists():
                # username already exists
                return render(request, "Dailyjotter/main-page.html")
            else:
                context = { 'message' : "User not found, Please retry",
                            'form' : form}
                return render(request, "Dailyjotter/login.html", context)

   return render(request, "Dailyjotter/login.html", { 'form' : form})



class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "Dailyjotter/sign-up.html", {'form': form})

    def post(self, request):

        form =  SignUpForm(request.POST)
        if form.is_valid():
            usernames = Author.objects.values_list('username', flat=True)
            username = form.cleaned_data.get('Username')
            first_name = form.cleaned_data.get('Firstname')
            surname = form.cleaned_data.get('Lastname')
            password = form.cleaned_data.get('Password')

            new_user = Author(username=username, first_name=first_name, surname=surname, password=password)


            passwords = Author.objects.values_list('password', flat=True)
            password = form.cleaned_data.get('password')

            if username in usernames and password in passwords :
                print("Cant create account ")
            else :
                new_user.save()
                return HttpResponse("User Saved")



        return render(request, "Dailyjotter/sign-up.html", {'form' : form})
                


    

class CreatePostView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


