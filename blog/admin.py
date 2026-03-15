from django.contrib import admin
from .models import Post, Comment, CommentLikes

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at') # Fields to display in the list view
    search_fields = ('title',) # Add a search bar for 'title'
    list_filter = ('created_at',) # Add filters for 'created_at'



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'comment') 
    search_fields = ('user__username', 'post__title', 'comment') 
    list_filter = ('user',)


@admin.register(CommentLikes)    
class CommentLikesAdmin(admin.ModelAdmin):
    list_display = ('user', 'post') 
    search_fields = ('user__username', 'post__title') 
    list_filter = ('user',)