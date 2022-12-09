from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from .forms import RegisterForm
# Create your views here.

def register(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            messages.success(request,f'welcome {username} your account is created , Now you can login')
            return redirect (reverse('index'))
            
    else:
        form = RegisterForm()
            
    context={
       "form" :form
    }
    return render(request, "users/register.html", context)
