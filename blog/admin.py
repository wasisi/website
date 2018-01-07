from django.contrib import admin

# Register your models here.
from .models import Post

# Tell Django admin site that model is registered in admin site using 
# custom class that inherits from ModelAdmin.
class PostAdmin(admin.ModelAdmin):
# Determine how posts are to be displayed in the admin dashboard  
   list_display = ('title', 'slug', 'author', 'publish',
                   'status')
# Additional field for filtering, searching and ordering   
# Right sidebar added to allow filtering by fields in list_filter attribute
   list_filter = ('status', 'created', 'publish', 'author')
# Searchable fields using the search_fields attribute.   
   search_fields = ('title', 'body')
# Prepopulate slug url using title   
   prepopulated_fields = {'slug': ('title',)}
# Look up widget to replace dropdown. Useful when you have many users   
   raw_id_fields = ('author',)
# Bar to navigate quickly through a date hierarchy   
   date_hierarchy = 'publish'
   ordering = ['status', 'publish']
# Register classes
admin.site.register(Post, PostAdmin)