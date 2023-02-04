from django.contrib import admin

from .models import *


class TagInline(admin.TabularInline):
    model = Post.tag.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [TagInline]
