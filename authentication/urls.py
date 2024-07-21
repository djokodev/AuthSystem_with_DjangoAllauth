
from django.urls import path
from authentication.views import loginPage, home, logout_view

urlpatterns = [
  path("", loginPage, name="login"),
  path("home/", home, name="home"),
  path("logout/", logout_view, name="logout"),
]
