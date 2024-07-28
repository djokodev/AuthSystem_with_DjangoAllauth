
from django.urls import path
from authentication.views import loginView, home, logout_view
from authentication.views import test_celery


urlpatterns = [
  path("", loginView, name="login"),
  path("home/", home, name="home"),
  path("logout/", logout_view, name="logout"),
  path('test/', test_celery, name='test_celery'),
]
