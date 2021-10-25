from django.contrib import admin
from speak.models import Post, Like
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','text_of_post','data_created','user')
    list_filter = ('title',)
    search_fields = ['title']

class LikeAdmin(admin.ModelAdmin):
    list_display = ('id','post', 'user',)
    list_filter = ('user',)
    search_fields = ['post__title']

admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)