from django.contrib.auth.models import User
from .models import Event
from rest_framework import status
from rest_framework.test import APITestCase


class EventListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='rob', password='pass')

    def test_can_list_events(self):
        rob = User.objects.get(username='rob')
        Event.objects.create(owner=rob, title='a title')
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_an_event(self):
        self.client.login(username='rob', password='pass')
        response = self.client.post(
            '/events/', {'title': 'a title', 'place': 'my place'}
        )
        count = Event.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_event(self):
        response = self.client.post('/events/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class EventDetailViewTests(APITestCase):
    def setUp(self):
        rob = User.objects.create_user(username='rob', password='pass')
        nick = User.objects.create_user(username='nick', password='pass')
        Event.objects.create(
            owner=rob, title='rob title', content='Robs event'
        )
        Event.objects.create(
            owner=nick, title='nick title', content='Nicks event'
        )

    def test_can_retrieve_event_using_valid_id(self):
        response = self.client.get('/events/1/')
        self.assertEqual(response.data['title'], 'rob title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_event_using_invalid_id(self):
        response = self.client.get('/posts/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_event(self):
        self.client.login(username='rob', password='pass')
        response = self.client.put(
            '/events/1/', {'title': 'a new title', 'place': 'my place'}
        )
        event = Event.objects.first()
        self.assertEqual(event.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_event_they_dont_own(self):
        self.client.login(username='rob', password='pass')
        response = self.client.put(
            '/events/2/', {'title': 'a new title', 'place': 'my place'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
