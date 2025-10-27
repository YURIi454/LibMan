from enum import Enum, unique

from django.db import models
from django.db.models import CASCADE
from config.settings import AUTH_USER_MODEL
from library.models import Book


@unique
class StatusList(Enum):
    """ Статусы выданной книг. """

    READER_HAS = 1
    IN_LIBRARY = 2
    LOOSE = 0

    @property
    def label(self):
        """ Вывод удобочитаемого названия. """

        labels = {
            'READER_HAS': 'у читателя',
            'IN_LIBRARY': 'в библиотеке',
            'LOOSE': 'утеряна',
        }

        return labels[self.name]


class BookLoan(models.Model):
    """ Выдача книг. """

    reader = models.ForeignKey(AUTH_USER_MODEL, on_delete=CASCADE, verbose_name='читатель', related_name='reader')
    book = models.ManyToManyField(Book, verbose_name='книга', related_name='книга')
    status = models.PositiveSmallIntegerField(choices=[(tag.value, tag.label) for tag in StatusList], default=2,
                                              verbose_name='статус выдачи')

    date_get = models.DateTimeField(blank=True, null=True, verbose_name='дата выдачи')
    date_return = models.DateTimeField(blank=True, null=True, verbose_name='дата возврата')

    def __str__(self):
        return f'{self.reader}'

    class Meta:
        verbose_name = 'Выдача книг'
        verbose_name_plural = 'Выдачи книг'
        ordering = ['reader']
