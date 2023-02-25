from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from .models import Author,Post
from .forms import PostForm, LoginForm, SignUpForm
from django.utils.text import slugify
import dropbox
from dropbox.files import WriteMode
from django.conf import settings
import io
import json
import cloudinary
import cloudinary.uploader
import cloudinary.api


# Set up Cloudinary credentials
cloudinary.config(
  cloud_name = "dbd7rcwwx",
  api_key = "925952713517876",
  api_secret = "SoB33wLiLb8JSLJ1OKlpfSW3bfY"
)

latest_posts =  Post.objects.all().order_by("-id")[:7]

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

    latest_posts =  Post.objects.all().order_by("-id")[:7]
    author_id = request.session.get('author')
    live_author = Author.objects.get(id=author_id)
    print(latest_posts)

    context =  { 'posts' : latest_posts,
                'author' : live_author}
    return render(request, "Dailyjotter/main-page.html", context=context)



def test_main(request):

    latest_posts =  Post.objects.all().order_by("-date")[:3]
    print(len(latest_posts))

    return render(request, "Dailyjotter/main-page.html", { 'posts' : latest_posts})


def create_post(request):

    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid(): 

                    author_id = request.session.get('author')

                    author = Author.objects.get(id=author_id)
                    title = form.cleaned_data.get('title')
                    keynote = form.cleaned_data.get('excerpt')
                    image = form.cleaned_data.get('image')
                    content = form.cleaned_data.get('content')
                    original_slug = slugify(title)
                    unique_slug = original_slug
                    count = 1
                    while Post.objects.filter(slug=unique_slug).exists():
                        unique_slug = f'{original_slug}-{count}'
                        count += 1 
    
                 
                    new_post = form.save(commit=False) 
                    new_post.author = author
                    response = cloudinary.uploader.upload(image, public_id=f'images/{new_post.id}_{image.name}')
                    new_post.image_url = response['secure_url']
                    new_post.slug = unique_slug
                    print("Save successful ")
                    new_post.save()
                    return redirect("home")

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

        if author.image_url:
            public_id = author.image_url.split('/')[-1].split('.')[0] # Extract public ID from URL
            cloudinary.uploader.destroy(public_id)
            print("trying to delete")

        if 'image' in request.FILES:
            image = request.FILES['image']
            response = cloudinary.uploader.upload(image, public_id=f'images/{author.id}_{image.name}')
            author.image_url = response['secure_url']
            author.save()
        return redirect('Profile')  
    else:
        return redirect('Profile')  

def post_detail(request, slug):
   post = Post.objects.get(slug=slug)


   return render(request, "Dailyjotter/post-detail.html", {
      "post" : post
   })
   