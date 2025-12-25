from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import Post

# Create your views here.





def home(request):
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
        return redirect('create_blog')
       
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
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        image = request.FILES.get('image')

        post = Post.objects.create(title=title, content=content, author=author, image=image)
        return redirect('my_blogs')

    return render(request,'blog/create.html')


def my_blogs(request):
    posts = Post.objects.filter(author=request.user)
    context = {'posts': posts}
    return render(request,'blog/my_blogs.html',context)


def all_blogs(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,'blog/my_blogs.html',context)



def update_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.save()
        return redirect('my_blogs')

    context = {'post': post}
    return render(request, 'blog/update.html', context)


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('my_blogs')


def read_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blog/read.html', context)
    
   

