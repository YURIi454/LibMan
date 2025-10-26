import django_filters
from library.models import Book


class BookFilter(django_filters.FilterSet):
    """ Фильтр поиска книг. """

    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    authors = django_filters.CharFilter(method="filter_by_author")
    genres = django_filters.NumberFilter(
        field_name="genres__name")

    class Meta:
        model = Book
        fields = ["title", "authors", "genres"]

    def filter_by_author(self, queryset, name, value):
        return queryset.filter(authors__name=value)
