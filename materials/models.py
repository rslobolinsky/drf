from django.conf import settings
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=300, verbose_name='название')
    preview = models.ImageField(upload_to='courses/', verbose_name='превью', blank=True, null=True)
    description = models.TextField(verbose_name='описание', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', blank=True,
                              null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=300, verbose_name='название')
    preview = models.ImageField(upload_to='lessons/', verbose_name='превью', blank=True, null=True)
    description = models.TextField(verbose_name='описание', blank=True, null=True)
    url_video = models.URLField(verbose_name='ссылка на видео', blank=True, null=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', related_name='lesson')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', blank=True,
                              null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscribe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь',
                             related_name='subscribe')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', related_name='subscribe')

    def __str__(self):
        return f'Подписка пользователя {self.user} на курс {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
