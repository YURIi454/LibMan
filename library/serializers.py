from rest_framework import serializers
from library.models import Book, Genre
from book_loan.models import BookLoan
from authors.models import Author
from users.models import CustomUser


class AuthorSerializer(serializers.ModelSerializer):
    """ Сериализатор для авторов. """

    class Meta:
        model = Author
        fields = ['id', 'full_name', 'description']


class GenreSerializer(serializers.ModelSerializer):
    """ Сериализатор для жанров. """

    class Meta:
        model = Genre
        fields = ['name', 'description']


class BookSerializer(serializers.ModelSerializer):
    """ Сериализатор для книги. """

    authors = AuthorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            'title',
            'authors',
            'genres',
            'binding',
            'description',
            'condition',
            'edition',
            'preview',
        ]

    def get_authors_names(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])

    def get_genres_names(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя. """

    class Meta:
        model = CustomUser
        fields = ['id', 'username']


class BookLoanSerializer(serializers.ModelSerializer):
    """ Сериализатор для выдачи книг. """

    reader = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = BookLoan
        fields = [
            'reader',
            'book',
            'status',
            'date_get',
            'date_return',
        ]
