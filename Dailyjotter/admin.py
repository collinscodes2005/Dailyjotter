from django.contrib import admin
from .models import Post,Author
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('date', 'author', 'title')
    list_filter = ('date',)



admin.site.register(Author)
admin.site.register(Post, PostAdmin)

