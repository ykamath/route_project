from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, StatesForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = StatesForm(request.POST)
        if form.is_valid():
            picked = form.cleaned_data.get('state_name')
    else:
        form = StatesForm()
    return render(request, 'users/profile.html', {'form': form})
