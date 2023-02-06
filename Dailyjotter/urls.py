from django.urls import path
from . import views 


urlpatterns = [
    path('', views.indexPage),
    path('login/', views.loginView),
    path('home', views.main),
    path('create-post/', views.create_post, name="create-post"),
    path('signup/', views.SignUp),
] 


