from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from book_loan.models import BookLoan
from library.serializers import BookLoanSerializer
from users.permissions import AdminPermission


class CreateBookLoan(CreateAPIView):
    """  Создание выдачи книги. """

    serializer_class = BookLoanSerializer
    permission_classes = [IsAuthenticated, AdminPermission]
    filter_backends = [DjangoFilterBackend]


class UpdateBookLoan(UpdateAPIView):
    """  Редактирование выдачи книги. """

    serializer_class = BookLoanSerializer
    permission_classes = [IsAuthenticated, AdminPermission]
    filter_backends = [DjangoFilterBackend]


class ListBookLoan(ListAPIView):
    """  Список выдачи книги. """

    serializer_class = BookLoanSerializer
    permission_classes = [IsAuthenticated, AdminPermission]
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = (
            BookLoan.objects
            .select_related('reader')
            .prefetch_related('book__authors')
            .prefetch_related('book__genres')
        )
        return queryset


class DetailBookLoan(RetrieveAPIView):
    """  Детальная выдачи книги. """

    serializer_class = BookLoanSerializer
    permission_classes = [IsAuthenticated, AdminPermission]
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = (
            BookLoan.objects
            .select_related('reader')
            .prefetch_related('book__authors')
            .prefetch_related('book__genres')
        )
        return queryset


class DeleteBookLoan(DestroyAPIView):
    """  Удаление выдачи книги. """

    serializer_class = BookLoanSerializer
    permission_classes = [IsAuthenticated, AdminPermission]
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return BookLoan.objects.all()
