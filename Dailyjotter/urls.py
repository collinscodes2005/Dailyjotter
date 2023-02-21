from django.urls import path
from . import views 


urlpatterns = [
    path('', views.loginView),
    path('login/', views.loginView),
    path('home', views.main, name="home"),
    path('create-post/', views.create_post, name="create-post"),
    path('signup/', views.SignUp),
    path('profile/', views.Profile),
    

] 



