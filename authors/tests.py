from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from authors.models import Author
from users.models import CustomUser


class AuthorsAPITestCase(APITestCase):
    """ Тест модели автор. """

    def setUp(self):
        self.user = CustomUser.objects.create_superuser(
            email='test@test.com',
            username='admn',
            password='test_pass123'
        )
        self.client.force_authenticate(user=self.user)
        self.author_data = {
            "full_name": "John Doe",
            "description": "Test author"
        }

    def create_test_author(self):
        """ Создаем автора для тестов. """
        author = Author.objects.create(**self.author_data)
        return author

    def test_create_author(self):
        url = reverse('authors:author_create')
        response = self.client.post(url, self.author_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.get().full_name, 'John Doe')

    def test_get_authors_list(self):
        url = reverse('authors:author_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_author(self):
        author = Author.objects.create(**self.author_data)
        self.updated_data = {
            "full_name": "G_man",
            "description": "Updated test author"
        }
        url = reverse('authors:author_update', kwargs={'pk': author.pk})
        response = self.client.put(url, self.updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_author = Author.objects.get(pk=author.pk)
        self.assertEqual(updated_author.full_name, 'G_man')
        self.assertEqual(updated_author.description, 'Updated test author')

    def test_detail_author(self):
        author = Author.objects.create(**self.author_data)
        url = reverse('authors:author_detail', kwargs={'pk': author.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], 'John Doe')

    def test_delete_author(self):
        author = self.create_test_author()
        url = reverse('authors:author_delete', kwargs={'pk': author.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Author.DoesNotExist):
            Author.objects.get(pk=author.pk)
