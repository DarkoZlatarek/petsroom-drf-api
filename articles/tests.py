from django.contrib.auth.models import User
from .models import Article
from rest_framework import status
from rest_framework.test import APITestCase


class ArticleListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='rob', password='pass')

    def test_can_list_articles(self):
        rob = User.objects.get(username='rob')
        Article.objects.create(owner=rob, title='a title')
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_an_article(self):
        self.client.login(username='rob', password='pass')
        response = self.client.post(
            '/articles/', {'title': 'a title', 'content': 'article content'}
        )
        count = Article.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_article(self):
        response = self.client.post('/articles/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ArticleDetailViewTests(APITestCase):
    def setUp(self):
        rob = User.objects.create_user(username='rob', password='pass')
        nick = User.objects.create_user(username='nick', password='pass')
        Article.objects.create(
            owner=rob, title='rob title', content='Robs article'
        )
        Article.objects.create(
            owner=nick, title='nick title', content='Nicks article'
        )

    def test_can_retrieve_article_using_valid_id(self):
        response = self.client.get('/articles/1/')
        self.assertEqual(response.data['title'], 'rob title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_article_using_invalid_id(self):
        response = self.client.get('/articles/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_article(self):
        self.client.login(username='rob', password='pass')
        response = self.client.put(
            '/articles/1/', {'title': 'a new title', 'content': 'New article'}
            )
        article = Article.objects.filter(pk=1).first()
        self.assertEqual(article.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_article_they_dont_own(self):
        self.client.login(username='rob', password='pass')
        response = self.client.put(
            '/articles/2/', {'title': 'a new title', 'place': 'my place'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
