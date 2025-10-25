from django.urls import path

from book_loan import views

app_name = 'book_loan'

urlpatterns = [
    path('loan_create/', views.CreateBookLoan.as_view(), name='loan_create'),
    path('loan_update/', views.UpdateBookLoan.as_view(), name='loan_update'),
    path('loan_detail/', views.ListBookLoan.as_view(), name='loan_detail'),
    path('loan_list/', views.DetailBookLoan.as_view(), name='loan_list'),
    path('loan_delete/', views.DeleteBookLoan.as_view(), name='loan_delete'),

]
