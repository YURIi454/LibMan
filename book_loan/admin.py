from django.contrib import admin

from book_loan.models import BookLoan


@admin.register(BookLoan)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('reader', 'book', 'status', 'date_get', 'date_return',)
    search_fields = ('status',)
