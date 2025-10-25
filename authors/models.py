from django.db import models


class Author(models.Model):
    """ Автор. """

    full_name = models.CharField(max_length=200, verbose_name='полное имя')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='описание')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='изменён')

    def __str__(self):
        """ Вывод информации. """

        return f'{self.full_name},{self.description}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['created_at']
        indexes = [models.Index(fields=['full_name', ])]
        permissions = [
            ('administrator', 'редактирование автора'),
        ]
