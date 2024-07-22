
from django.urls import path
from authentication.views import loginView, home, logout_view

urlpatterns = [
  path("", loginView, name="login"),
  path("home/", home, name="home"),
  path("logout/", logout_view, name="logout"),
]
