from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('create_blog/',views.create_blog,name='create_blog'),
    path('my_blogs/',views.my_blogs,name='my_blogs'),

]