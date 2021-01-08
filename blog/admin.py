from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author', 'publish', 'status')
    exclude = ('like', 'views', 'publish')
    list_filter = ('status', 'author', 'publish')
    search_fields = ('title', 'body', 'author')
    prepopulated_fields = {"slug" : ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

#admin.site.register(Post, PostAdmin)