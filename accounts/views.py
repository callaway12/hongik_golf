from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            profile = User.objects.profile(hak=request.POST['hak'], jungong=request['jungong'], phone=request['phone'],gisu=request['gisu'])
            profile.save()
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'asdfasdvx'
    user.save()



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        redirect('home')
    return render(request, 'home.html')

def main(request):
    return render(request, 'main.html')
