from django.urls import path
from . import views
from .views import validate_username

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register', views. RegisterView.as_view(), name='register'),
    path('validate_username', validate_username, name='validate_username')

]
