# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from bookmarks.models import *
class LinkAdmin(admin.ModelAdmin):
    pass


# Register your models here.
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'user')
    list_filter = ('user',)
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(Link, LinkAdmin)    
admin.site.register(Bookmark, BookmarkAdmin)  