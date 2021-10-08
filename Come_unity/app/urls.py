from django.urls import path
from app import views

urlpatterns = [
    # path("", views.home, name="home"),
    path('', views.index),
    path("signin", views.signin, name="signin"),
    path("info", views.info, name="info"),

]