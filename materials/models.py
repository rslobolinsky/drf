from django.db import models


class Course(models.Model):

    name = models.CharField(max_length=300, verbose_name='название')
    preview = models.ImageField(upload_to='courses/', verbose_name='превью', blank=True, null=True)
    description = models.TextField(verbose_name='описание', blank=True, null=True)

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

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
