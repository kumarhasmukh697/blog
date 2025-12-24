from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at') # Fields to display in the list view
    search_fields = ('title',) # Add a search bar for 'title'
    list_filter = ('created_at',) # Add filters for 'created_at'



