from django.urls import path
from app import views

urlpatterns = [
    # path("", views.home, name="home"),
    path('', views.index),
    # path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    
    path('signin', views.signin, name="signin"),
    path('receive', views.receive)
]