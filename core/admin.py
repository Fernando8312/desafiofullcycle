from django.contrib import admin
from core.models import Post, Tags
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('title','created_at','tags__name')
    search_fields = ('title','created_at','tags__name')
    list_filter=('tags', 'created_at')

admin.site.register(Post, PostsAdmin)
admin.site.register(Tags)