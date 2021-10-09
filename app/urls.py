from django.urls import path
from app import views

urlpatterns = [
    path("signin", views.signin, name="signin"),
    #path("signup", views.signup, name="signup"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("form", views.form, name="form"),
    path("community", views.community, name="community"),
    path("info", views.info, name="info"),
]
