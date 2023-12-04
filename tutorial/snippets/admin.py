# myapp/admin.py
from django.contrib import admin
from .models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'style', 'created')
    list_filter = ('language', 'style', 'created')
    search_fields = ('title', 'code')
    date_hierarchy = 'created'
    ordering = ('created',)

admin.site.register(Snippet, SnippetAdmin)
