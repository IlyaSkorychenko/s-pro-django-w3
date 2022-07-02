from django.urls import path
from bookstore import views

urlpatterns = [
    path('', views.all_books, name='all-books'),
    path('create', views.books_creation_handler),
]
