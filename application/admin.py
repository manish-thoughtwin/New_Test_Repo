from django.contrib import admin
from .models import Registration,Blogs

# Register your models here.from
admin.site.register(Registration)



class BlogAdmin(admin.ModelAdmin):
  list_display = ("title",)
  prepopulated_fields = {"slug": ("title",)} 
     
admin.site.register(Blogs, BlogAdmin)  



# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'author', 'created_on', 'status')
#     list_filter = ('status', 'created_on', 'author')
#     search_fields = ('title', 'content')
#     prepopulated_fields = {'slug': ('title',)}
#     raw_id_fields = ('author',)
#     date_hierarchy = 'created_on'
#     ordering = ('status', 'created_on')

