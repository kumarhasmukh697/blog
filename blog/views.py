from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.





def home(request):
    user = request.user
    print(user)
    return render(request, 'blog/login_register.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password != confirm_password:
            return HttpResponse("Passwords do not match!")

        user = User.objects.create_user(username=username,password=password)
        login(request, user)
        return render(request,'blog/create.html')
       

    return render(request, 'blog/login_register.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user = request.user
            context = {'user': user}
            return render(request, 'blog/create.html',context)
        else:
            return HttpResponse("Invalid credentials, please try again.")
    return render(request, 'blog/login_register.html')



def create_blog(request):
    return render(request,'blog/create.html')

def my_blogs(request):
    return render(request,'blog/my_blogs.html')
   

