from django.contrib import admin
from .models import Post, Profile

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, PostAdmin)
