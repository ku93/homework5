from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.ru')
        self.course = Course.objects.create(name='Модуль 1', owner=self.user)
        self.lesson = Lesson.objects.create(name='Урок 1', course=self.course, owner=self.user,
                                            link_to_the_video='https://youtube.com')
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('name'), self.course.name)

    def test_course_create(self):
        url = reverse('materials:course-list')
        data = {
            'name': 'Модуль 2',
            'owner': self.user.pk
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)

    def test_course_update(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        data = {
            'name': 'Новое название модуля'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('name'), 'Новое название модуля')

    def test_course_delete(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)

    def test_course_list(self):
        url = reverse('materials:course-list')
        response = self.client.get(url)
        data = response.json()

        resuli = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "name": self.course.name,
                    "preview": None,
                    "description": None,
                    "owner": self.course.owner.pk
                },
            ]
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, resuli)


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.ru')
        self.course = Course.objects.create(name='Модуль 1', owner=self.user)
        self.lesson = Lesson.objects.create(name='Урок 1', course=self.course, owner=self.user,
                                            link_to_the_video='https://youtube.com')
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lesson-retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('name'), self.lesson.name)

    def test_lesson_create(self):
        url = reverse('materials:lesson-create')
        data = {
            'name': 'Урок 2',
            "link_to_the_video": "https://www.youtube.com/watch?v=Q4Ma8FSZpfY.youtube.com",
            'course': self.course.pk,
            'owner': self.user.pk
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 2)

    def test_lesson_update(self):
        url = reverse('materials:lesson-update', args=(self.lesson.pk,))
        data = {
            'name': 'Новое название урока'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('name'), 'Новое название урока')

    def test_lesson_delete(self):
        url = reverse('materials:lesson-destroy', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 0)

    def test_lesson_list(self):
        url = reverse('materials:lesson-list')
        response = self.client.get(url)
        data = response.json()

        resuli = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "link_to_the_video": self.lesson.link_to_the_video,
                    "name": self.lesson.name,
                    "description": None,
                    "preview": None,
                    "course": self.course.pk,
                    "owner": self.user.pk
                },
            ]
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, resuli)
