from django.contrib.auth.models import AbstractUser
from django.db import models
from users.validators import UsernameValidator

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'


class User(AbstractUser):

    roles = (
        (USER, USER),
        (MODERATOR, MODERATOR),
        (ADMIN, ADMIN),
    )
    username_validator = UsernameValidator()
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,
        validators=[username_validator],
    )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField('Email', max_length=254, unique=True)
    role = models.CharField(
        'Роль пользователя',
        choices=roles,
        max_length=max(len(role[1]) for role in roles), default=USER
    )
    bio = models.TextField('Биография', blank=True)
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=100,
        null=True
    )

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELDS = 'email'

    def __str__(self):
        return str(self.username)

    @property
    def is_admin(self):
        """Проверка пользователя на наличие прав администратора."""
        return self.role == "admin" or self.is_superuser

    @property
    def is_moderator(self):
        """Проверка пользователя на наличие прав модератора."""
        return self.role == "moderator"

    @property
    def is_user(self):
        """Проверка пользователя на наличие стандартных прав."""
        return self.role == "user"

    class Meta:
        ordering = ('username',)

        def __init__(self):
            self.username = None

        def __str__(self):
            return self.username
