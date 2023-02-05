from django.urls import path
from . import views 


urlpatterns = [
    path('', views.indexPage),
    path('login/', views.loginView),
    path('home', views.main),
    path('signup/', views.SignUp),
] 


