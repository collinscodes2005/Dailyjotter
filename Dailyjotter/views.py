from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from .models import Author,Post
from .forms import PostForm, LoginForm, SignUpForm
from django.utils.text import slugify


latest_posts =  Post.objects.all().order_by("-date")[:3]

# Create your views here.
def indexPage(request):


       return render(request, "Dailyjotter/login.html")


def loginView(request):
   form = LoginForm() 
   if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():

            usernames = Author.objects.values_list('user_name', flat=True)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            

            if Author.objects.filter(user_name=username).exists() and Author.objects.filter(password=password).exists():
                # username already exists
                author = Author.objects.filter(user_name=username, password=password).first()

                authored = Author.objects.get(id=author.id)

                    #creating author session 
                request.session['author'] = author.id

                return render(request, "Dailyjotter/main-page.html", { 'posts' : latest_posts})
                
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
            bio = form.cleaned_data.get('bio')

            new_user = Author(first_name=firstname, surname=surname,user_name=username,  password=password, about=bio)


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
        form = PostForm(request.POST, request.FILES)
        if form.is_valid(): 

                    author_id = request.session.get('author_id')

                    author = Author.objects.get(id=author_id)

                    #creating author session 
                    request.session['author'] = author

                    title = form.cleaned_data.get('title')
                    keynote = form.cleaned_data.get('excerpt')
                    imager = form.cleaned_data.get('image')
                    content = form.cleaned_data.get('content')
                   
                    original_slug = slugify(title)
                    unique_slug = original_slug
                    count = 1

                    while Post.objects.filter(slug=unique_slug).exists():
                        unique_slug = f'{original_slug}-{count}'
                        count += 1 

                    new_post = form.save(commit=False) 
                    new_post.author = author
                    new_post.image = form.cleaned_data['image']
                    new_post.slug = unique_slug
                    print("jeeezzz")
                    new_post.save()

                    return redirect('home')


            
        else :
          print("damnnnn!!")
          print("Form errors:", form.errors)
          form = PostForm()
    else:
        print("shitttttttt")

    return render(request, "Dailyjotter/create-post.html", {'form' : form })

def Profile(request):

    author_id =  request.session.get('author')
    author = Author.objects.get(id=author_id)


    return render(request, "Dailyjotter/profile.html", {
        'author' : author
    })


'''fuction to edit profile images '''
def update_profile_image(request):
    if request.method == 'POST':
        author_id =  request.session.get('author')
        author = Author.objects.get(id=author_id)

        if 'image' in request.FILES:
            author.image = request.FILES['image']
            author.save()
        return redirect('Profile')  
    else:
        return redirect('Profile')  