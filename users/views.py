from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'welcome {username}, your account is created.')
            return redirect('food:items')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form':form})

def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('food:items')