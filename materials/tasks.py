import datetime
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from materials.models import Course
from users.models import User


@shared_task
def notify_subscribers_about_course_update(course_id):
    all_email_list = []
    course = Course.objects.get(id=course_id)
    all_subs = course.subscribe.all()
    for sub in all_subs:
        email = sub.user.email
        all_email_list.append(email)
        
    for email in all_email_list:
        send_mail(
            subject='Обновление курса',
            message='Ваш курс был обновлен',
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
        )
        print(f'Письмо было отправлено на адрес {email}')

