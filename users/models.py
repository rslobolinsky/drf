from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', null=True, blank=True)
    city = models.CharField(max_length=100, verbose_name='город', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Payment(models.Model):
    CASH = 'cash'
    TRANSLATION = 'transfer'

    METHODS = (
        (CASH, 'Наличными'),
        (TRANSLATION, 'Перевод на счет'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='payment')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', related_name='payment', null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок', related_name='payment', null=True, blank=True)

    date = models.DateField(auto_now_add=True, verbose_name='дата платежа')
    sum = models.PositiveIntegerField(verbose_name='сумма платежа')
    pay_method = models.CharField(max_length=10, choices=METHODS, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user} за {self.course if self.course else self.lesson }, {self.sum} руб. ({self.date})'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ('-date',)
