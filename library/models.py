from enum import Enum, unique

from django.db import models

from authors.models import Author


@unique
class BindingList(Enum):
    """ Тип переплёта. """

    SOFT = 1
    HARD = 2
    NOT_DEF = 0

    @property
    def label(self):
        """ Вывод удобочитаемого названия. """

        labels = {
            'SOFT': 'мягкий',
            'HARD': 'твёрдый',
            'NOT_DEF': 'не определён',
        }

        return labels[self.name]


@unique
class EditionList(Enum):
    """ Тип книги. """

    PRINTED = 1
    ELECTRO = 2
    NOT_DEF = 0

    @property
    def label(self):
        """ Вывод удобного текста. """

        labels = {
            'PRINTED': 'печатная',
            'ELECTRO': 'электронная',
            'NOT_DEF': 'не определён',
        }

        return labels[self.name]


@unique
class ConditionList(Enum):
    """ Состояние книги. """

    NEW = 1
    GOOD = 2
    BAD = 3

    @property
    def label(self):
        """ Вывод удобочитаемого названия. """

        labels = {
            'NEW': 'новая',
            'GOOD': 'хорошая',
            'BAD': 'на списание',
        }

        return labels[self.name]


@unique
class GenreList(Enum):
    """ Жанры книг. """

    SCIENCE = 1
    NATURE = 2
    FOOD = 3
    HEALTH = 4
    CARS = 5
    PEOPLE = 6
    BUSINESS = 7
    HOBBY = 8
    NOT_DEF = 0

    @property
    def label(self):
        """ Вывод удобочитаемого названия. """

        labels = {
            'SCIENCE': 'наука',
            'NATURE': 'природа',
            'FOOD': 'еда',
            'HEALTH': 'здоровье',
            'CARS': 'автомобили',
            'PEOPLE': 'люди',
            'BUSINESS': 'бизнес',
            'HOBBY': 'хобби',
            'NOT_DEF': 'не определён',
        }

        return labels[self.name]


class Genre(models.Model):
    """ Жанр. """

    name = models.CharField(choices=[(tag.value, tag.label) for tag in GenreList], default=0,
                            verbose_name='жанр')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='описание')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='изменён')

    def __str__(self):
        """ Вывод информации. """

        return f'{self.name},{self.description}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['created_at']
        permissions = [
            ('genre_redact', 'редактирование жанра'),
        ]


class Book(models.Model):
    """ Книга. """

    title = models.CharField(unique=True, max_length=200, verbose_name='название')
    authors = models.ManyToManyField(Author, verbose_name='автор', related_name='authors')
    genres = models.ManyToManyField('Genre', verbose_name='жанр', related_name='genre')
    binding = models.IntegerField(choices=[(tag.value, tag.label) for tag in BindingList], default=0,
                                  verbose_name='переплет')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='описание')
    condition = models.IntegerField(choices=[(tag.value, tag.label) for tag in ConditionList],
                                    default=1,
                                    verbose_name='состояние')
    edition = models.IntegerField(choices=[(tag.value, tag.label) for tag in EditionList], default=0,
                                  verbose_name='тип')
    preview = models.URLField(max_length=500, blank=True, verbose_name='Ссылка на предпросмотр')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='изменён')

    def __str__(self):
        """ Вывод информации. """

        return f'{self.title}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['created_at']
        permissions = [
            ('bookworm', 'редактирование книг'),
        ]
