from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
# from django.contrib.auth.forms import UserCreationForm

from users.forms import SignUpForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('districts')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})