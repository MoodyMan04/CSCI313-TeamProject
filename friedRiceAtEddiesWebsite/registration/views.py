from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm
from checkout.models import Member
from django.contrib.auth.models import User

# def add_to_member(new_user):
#     member = Member.objects.get()
#     try:
#         u, created = Member.objects.get_or_create(member=member, user=Member.objects.get(user=request.user))
#     except:
#         u, created = Member.objects.get_or_create(member=member)
#     u.save()
#     return u

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', { 'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            # Member.user = user # <- this silly lil piece of code works but overrides the previous member
            user.save()
            messages.success(request, 'Account creation successful. Please enjoy the rice.')
            login(request, user)
            return redirect('menu')
        else:
            return render(request, 'registration/register.html', {'form':form}) 

def sign_in(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(
                    request, f'Hi {username.title()}, welcome back!')
                return redirect('menu')

        # either form not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'users/login.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('login')
