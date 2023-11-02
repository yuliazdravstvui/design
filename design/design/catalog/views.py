from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.forms import RegisterUserForm



def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'registration/login.html')

def logout(request):
    return render(request, 'registration/logout.html')

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')

