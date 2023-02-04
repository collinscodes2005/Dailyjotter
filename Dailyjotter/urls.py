from django.urls import path
from . import views 

urlpatterns = [
    path('', views.indexPage),
    path('login/', views.loginView),
    path('create-post/', views.CreatePostView.as_view()),
    path('signup/', views.SignUp),

    
]


