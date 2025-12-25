from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('create_blog/',views.create_blog,name='create_blog'),
    path('my_blogs/',views.my_blogs,name='my_blogs'),
    path('all_blogs/',views.all_blogs,name='all_blogs'),
    path('update_post/<int:post_id>/', views.update_post, name='update_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('read_post/<int:post_id>/', views.read_post, name='read_post'),

]