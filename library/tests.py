from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from authors.models import Author
from library.models import Book, Genre
from users.models import CustomUser


class LibraryAPITestCase(APITestCase):
    """ Тест модели книга. """

    def setUp(self):
        self.user = CustomUser.objects.create_superuser(
            email='test@test.com',
            username='admn',
            password='test_pass123')
        self.author = Author.objects.create(full_name='Carl', description=' _ ')
        self.genres = Genre.objects.create()
        self.client.login(email='test@test.com', username='test', password='test_pass123', is_staff=True)
        self.client.force_authenticate(user=self.user)
        self.book_data = {
            "title": "TEST_BOOK",
            "authors": [self.author.id],
            "genres": [self.genres.id],
        }

    def create_test_book(self):
        """ Создаем книгу для тестов. """

        book = Book.objects.create(title="TEST_BOOK", )

        book.authors.set([self.author])
        book.genres.set([self.genres])

        return book

    def test_create_book(self):
        url = reverse('library:book_create')
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.get().title, 'TEST_BOOK')

    def test_get_books_list(self):
        book = Book.objects.create(title="TEST_BOOK", )
        book.authors.set([self.author])
        book.genres.set([self.genres])
        url = reverse('library:book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_book(self):
        book = Book.objects.create(title="TEST_BOOK", )
        book.authors.set([self.author])
        book.genres.set([self.genres])
        self.updated_data = {
            "title": "TEST_AGAIN",
            "authors": [self.author.id],
            "genres": [self.genres.id]
        }
        url = reverse('library:book_update', kwargs={'pk': book.pk})
        response = self.client.put(url, self.updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_book = Book.objects.get(pk=book.pk)
        self.assertEqual(updated_book.title, 'TEST_AGAIN')
        self.assertIn(self.author, updated_book.authors.all())
        self.assertIn(self.genres, updated_book.genres.all())

    def test_delete_book(self):
        book = self.create_test_book()
        url = reverse('library:book_delete', kwargs={'pk': book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(pk=book.pk)
