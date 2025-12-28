from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import Post,Comment,CommentLikes

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
    post = get_object_or_404(Post, id=post_id)
    liked = False
    if request.user.is_authenticated:
        liked = CommentLikes.objects.filter(user=request.user, post=post).exists()
    context = {'post': post, 'user': request.user, 'liked': liked}
    return render(request, 'blog/read.html', context)



@login_required
def toggle_like(request, post_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=400)
    post = get_object_or_404(Post, id=post_id)
    like_obj = CommentLikes.objects.filter(user=request.user, post=post).first()
    if like_obj:
        # unlike
        like_obj.delete()
        if post.likes > 0:
            post.likes -= 1
            post.save()
        liked = False
    else:
        # like
        CommentLikes.objects.create(user=request.user, post=post)
        post.likes += 1
        post.save()
        liked = True
    return JsonResponse({'liked': liked, 'likes_count': post.likes})



@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        comment_text = request.POST.get('comment', '').strip()
        if comment_text:
            Comment.objects.create(user=request.user, post=post, comment=comment_text)
    return redirect('read_post', post_id=post_id)    
   
    
   

