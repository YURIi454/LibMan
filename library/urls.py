from django.urls import path

from library import views

app_name = 'library'

urlpatterns = [
    path('book_create/', views.CreateBook.as_view(), name='book_create'),
    path('book_update/<int:pk>/', views.UpdateBook.as_view(), name='book_update'),
    path('book_list/', views.ListBook.as_view(), name='book_list'),
    path('book_detail/<int:pk>/', views.DetailBook.as_view(), name='book_detail'),
    path('book_delete/<int:pk>/', views.DeleteBook.as_view(), name='book_delete'),
]
