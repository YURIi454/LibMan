from django.urls import path
from authors import views

app_name = 'authors'

urlpatterns = [

    path('author_create/', views.CreateAuthor.as_view(), name='author_create'),
    path('author_update/<int:pk>/', views.UpdateAuthor.as_view(), name='author_update'),
    path('author_detail/<int:pk>/', views.DetailAuthor.as_view(), name='author_detail'),
    path('author_list/', views.ListAuthor.as_view(), name='author_list'),
    path('author_delete/<int:pk>/', views.DeleteAuthor.as_view(), name='author_delete'),

]
