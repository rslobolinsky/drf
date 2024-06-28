from django.contrib.auth.models import Group
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from materials.models import Course, Lesson, Subscribe
from users.models import User


class LessonTestOwnerNotModerCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(pk=1, email='admin@sky.ru', password='qwerty')

        self.course = Course.objects.create(pk=1, name='Biology', owner=self.user)
        self.lesson = Lesson.objects.create(name='Fauna', url_video='http://video.youtube.com', owner=self.user,
                                            course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lesson_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        print('retrieve')
        print(response.json())
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'),
            self.lesson.name
        )

    def test_lesson_list(self):
        url = reverse('materials:lesson_list')
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_lesson_create(self):
        url = reverse('materials:lesson_create')
        data = {
            "name": "Flora",
            "url_video": 'http://video.youtube.com',
            "course": 1,
            "owner": 1
        }
        response = self.client.post(url, data=data)
        data = response.json()
        print(data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            data.get('name'),
            'Flora'
        )

    def test_lesson_update(self):
        url = reverse('materials:lesson_update', args=(self.lesson.pk,))
        data = {
            "name": "Flora",
            "url_video": "http://www.youtube.com"
        }
        response = self.client.patch(url, data=data)
        print(response.json())
        self.assertEqual(
            data.get('name'),
            "Flora"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_delete(self):
        url = reverse('materials:lesson_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        print(response.json())
        self.assertEqual(
            Lesson.objects.all().count(),
            0
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class LessonTestModerNotOwnerCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(pk=1, email='admin@sky.ru', password='qwerty')
        self.user2 = User.objects.create(pk=2, email='test@sky.pro', password='123456')
        Group.objects.create(name='moders')
        moder_group = Group.objects.get(name='moders')
        moder_group.user_set.add(self.user)
        self.course = Course.objects.create(pk=1, name='Biology', owner=self.user2)
        self.lesson = Lesson.objects.create(name='Fauna', url_video='http://video.youtube.com', owner=self.user2,
                                            course=self.course)
        self.client.force_authenticate(user=self.user)
    def test_lesson_retrieve(self):
        url = reverse('materials:lesson_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        print('retrieve')
        print(response.json())
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'),
            self.lesson.name
        )
    def test_lesson_list(self):
        url = reverse('materials:lesson_list')
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
    def test_lesson_create(self):
        url = reverse('materials:lesson_create')
        data = {
            "name": "Zoo",
            "url_video": 'http://video.youtube.com',
            "course": 1,
            "owner": 1
        }
        response = self.client.post(url, data=data)
        data = response.json()
        print(data)
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
    def test_lesson_update(self):
        url = reverse('materials:lesson_update', args=(self.lesson.pk,))
        data = {
            "name": "Flora",
            "url_video": "http://www.youtube.com"
        }
        response = self.client.patch(url, data=data)
        print(response.json())
        self.assertEqual(
            data.get('name'),
            "Flora"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
    def test_lesson_delete(self):
        url = reverse('materials:lesson_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email="test@test.ru")
        self.course = Course.objects.create(name="sub_test", description="sub_test", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscribe(self):
        Subscribe.objects.create(course=self.course, user=self.user)
        url = reverse("materials:set_subscribe", args=(self.course.pk,))
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'message': 'подписка удалена'}
        )

    def test_unsubscribe(self):
        url = reverse("materials:set_subscribe", args=(self.course.pk,))
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'message': 'подписка добавлена'}
        )