from django.urls import path
from . import views 

urlpatterns = [
    path('', views.IndexPageView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('create-post/', views.CreatePostView.as_view()),
    
]


