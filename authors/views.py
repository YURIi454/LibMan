from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from authors.models import Author
from library.serializers import AuthorSerializer
from users.permissions import AdminPermission


class CreateAuthor(CreateAPIView):
    """  Добавление автора. """

    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, AdminPermission]
    filter_backends = [DjangoFilterBackend]


class UpdateAuthor(UpdateAPIView):
    """  Редактирование автора. """

    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, AdminPermission]
    filter_backends = [DjangoFilterBackend]
    lookup_field = 'pk'

    def get_queryset(self):
        return Author.objects.all()


class ListAuthor(ListAPIView):
    """  Список авторов. """

    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return Author.objects.all()


class DetailAuthor(RetrieveAPIView):
    """  Детальная информация об авторе. """

    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return Author.objects.all()


class DeleteAuthor(DestroyAPIView):
    """  Удаление автора. """

    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, AdminPermission]
    filter_backends = [DjangoFilterBackend]
    lookup_field = 'pk'

    def get_queryset(self):
        return Author.objects.all()
