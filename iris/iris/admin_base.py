# Django modules
from django.contrib import admin


class AdminBase(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_per_page = 10
    ordering = ['id']
