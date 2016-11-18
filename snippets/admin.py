from django.contrib import admin

# Register your models here.
from .models import Snippets

class SnippetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Snippets, SnippetAdmin)