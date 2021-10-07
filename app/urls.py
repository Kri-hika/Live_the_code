from django.urls import path
from app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
]