from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from library.models import (
    Book,
)
from library.serializers import (
    BookSerializer,
)
from library.services import BookFilter
from users.permissions import AdminPermission


class CreateBook(CreateAPIView):
    """  Создание книги. """

    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, AdminPermission]
    filter_backends = [DjangoFilterBackend]


class UpdateBook(UpdateAPIView):
    """  Редактирование книги. """

    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, AdminPermission]
    filter_backends = [DjangoFilterBackend]
    lookup_field = 'pk'

    def get_queryset(self):
        return Book.objects.prefetch_related("authors")


class ListBook(ListAPIView):
    """  Список книг. """

    serializer_class = BookSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = BookFilter
    search_fields = ['title']
    ordering_fields = ['title', 'created_at']

    def get_queryset(self):
        """ Доступ всем. """

        return Book.objects.prefetch_related("authors")


class DetailBook(RetrieveAPIView):
    """  Детальная информация о книге. """

    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        """ Доступ всем. """

        return Book.objects.prefetch_related("authors")


class DeleteBook(DestroyAPIView):
    """  Удаление книги. """

    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, AdminPermission]
    filter_backends = [DjangoFilterBackend]
    lookup_field = 'pk'

    def get_queryset(self):
        """ Модератор и админ. """

        return Book.objects.all()
