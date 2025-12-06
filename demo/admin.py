from django.contrib import admin
from .models import Visitor

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'visited_at', 'ip_address']
    list_filter = ['visited_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['visited_at']