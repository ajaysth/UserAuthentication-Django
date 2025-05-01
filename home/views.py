from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate , login
from django.shortcuts import redirect

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect( '/userlogin')
    
    return render(request, 'index.html')


def userlogin(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html')
        
        
    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('/userlogin')
    # return render(request, 'index.html')
    
