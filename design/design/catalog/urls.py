from django.urls import path
from . import views
from .views import validate_username
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view, name='login'),
    path('logout/', LogoutView.as_view, name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('validate_username', validate_username, name='validate_username')

]
