from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .models import Author,Post
from .forms import PostForm, LoginForm

# Create your views here.
class IndexPageView(View):
    def get(self, request):
        return render(request, "Dailyjotter/base.html")

class LoginView(View):
   

    def get(self, request):
        form = LoginForm()
        return render(request, "Dailyjotter/login.html", { 'form' : form})


    def post(Self, request):

        form = LoginForm(request.POST)

        if form.is_valid():

            usernames = Author.objects.values_list('username', flat=True)
            username = form.cleaned_data.get('username')

            if username in usernames:
                # code to log the user in
                return render(request, "Dailyjotter/create_post.html")
                pass
            else:
                # code to return an error message
                pass
        
    
            return HttpResponseRedirect("/thank-you")

        return render(request, "Dailyjotter/login.html", { 'form' : form})


class CreatePostView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass


