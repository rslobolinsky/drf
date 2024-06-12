# Generated by Django 5.0.6 on 2024-06-09 16:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_alter_lesson_course'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='дата платежа')),
                ('sum', models.PositiveIntegerField(verbose_name='сумма платежа')),
                ('pay_method', models.CharField(choices=[('cash', 'Наличными'), ('translation', 'Перевод на счет')], verbose_name='способ оплаты')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='materials.course', verbose_name='курс')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='materials.lesson', verbose_name='урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
                'ordering': ('-date',),
            },
        ),
    ]
