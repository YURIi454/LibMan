from django.contrib import admin

from book_loan.models import BookLoan


# @admin.register(BookLoan)
# class UsersAdmin(admin.ModelAdmin):
#     list_display = ('reader', 'book', 'status', 'date_get', 'date_return',)
#     search_fields = ('status',)


@admin.register(BookLoan)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('reader', 'books', 'status', 'date_get', 'date_return',)
    search_fields = ('status',)

    def books(self, obj):
        return ", ".join(str(book) for book in obj.book.all())

    books.short_description = 'книги'
