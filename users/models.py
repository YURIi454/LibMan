from enum import Enum
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser


class StatusListUsers(Enum):
    """ Статусы пользователя. """

    NEW = 1
    STANDARD = 2
    MEDIUM = 3
    VIP = 4
    WAIT = 5
    BLOCKED = 0

    @property
    def label(self):
        """ Вывод удобного текста. """

        labels = {
            'NEW': 'новый',
            'STANDARD': 'обычный',
            'MEDIUM': 'проверенный',
            'VIP': 'надёжный',
            'WAIT': 'не подтверждён',
            'BLOCKED': 'заблокирован',
        }
        return labels[self.name]


class CustomUser(AbstractUser):
    """ Пользователь. """

    email = models.EmailField(unique=True, verbose_name='ваш email')
    username = models.CharField(max_length=150, help_text='Обязательно. '
                                                          'Не более 150 символов.'
                                                          ' Только буквы, цифры и @/./+/-/_.', null=True, blank=True,
                                verbose_name='имя')
    avatar = models.URLField(default='www.add_your_avatar.com', verbose_name='аватар')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='номер')
    status = models.IntegerField(choices=[(tag.value, tag.label) for tag in StatusListUsers],
                                 default=1,
                                 verbose_name='статус')
    activate_token = models.UUIDField(default=uuid4, editable=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='изменён')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", ]

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
