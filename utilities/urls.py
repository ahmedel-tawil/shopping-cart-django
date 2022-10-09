from django.contrib import admin
from django.urls import path
from . import views



app_name = "utilities"
urlpatterns = [
     path("signup/", views.signup, name="sign-up"),
     path("login_user", views.login_user, name="login_user"),
      path("logout_user", views.logout_user, name="logout_user"),

]

