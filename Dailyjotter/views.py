from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from .models import Author,Post
from .forms import PostForm, LoginForm, SignUpForm



# Create your views here.
def indexPage(request):


       return render(request, "Dailyjotter/index.html")


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
        pass

def SignUp(request):
    logForm = LoginForm()
    form = SignUpForm()
    if request.method == "POST":
        form =  SignUpForm(request.POST)
        if form.is_valid():


            usernames = Author.objects.values_list('user_name', flat=True)
            username = form.cleaned_data.get('username')
            firstname = form.cleaned_data.get('first_name')
            surname = form.cleaned_data.get('surname')
            password = form.cleaned_data.get('password')

            new_user = Author(first_name=firstname, surname=surname,user_name=username,  password=password)


            passwords = Author.objects.values_list('password', flat=True)
            password = form.cleaned_data.get('password')
            
            if username in usernames and password in passwords :
                print("Cant create account ")
                return render(request, "Dailyjotter/sign-up.html", {'form' : form,
                'err' : "user exists "})

            else :
                new_user.save()
                return render(request, "Dailyjotter/login.html", { 'form' : logForm,
                'success': "User created, login now"
                })

        else:
        # handle invalid form
            return render(request, "Dailyjotter/sign-up.html", {'form' : form, 'err' : "Form is invalid"})
    # else:
    #     form = SignUpForm()          
    return render(request, "Dailyjotter/sign-up.html", {'form' : form})

def main(request):

    latest_posts =  Post.objects.all().order_by("-date")[:3]

    return render(request, "Dailyjotter/main-page.html", { 'posts' : latest_posts})

def create_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            keynote = form.cleaned_data.get('excerpt')
            image = form.cleaned_data.get('image')
            content = form.cleaned_data.get('content')

            new_post = Post(title=title, excerpt=keynote, image=image)

            
    else :
        form = PostForm()

    return render(request, "Dailyjotter/create-post.html", {'form' : form })
