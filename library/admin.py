from django.contrib import admin

from library.models import Book


@admin.register(Book)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'display_authors',
                    'genres',
                    'binding',
                    'description',
                    'condition',
                    'edition',
                    'created_at',)
    list_filter = ('title',)
    search_fields = ('title',)

    def display_authors(self, obj):
        return ", ".join(str(author) for author in obj.authors.all())

    display_authors.short_description = 'авторы'
