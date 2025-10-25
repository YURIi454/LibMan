from django.contrib import admin

from authors.models import Author


@admin.register(Author)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'description', 'created_at',)
    list_filter = ('full_name',)
    search_fields = ('full_name',)
