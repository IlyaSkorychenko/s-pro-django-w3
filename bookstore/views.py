from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_GET, require_http_methods
from bookstore.forms import BookForm, SearchBookForm
from .models import Book


@require_GET
def all_books(request):
    search_form = SearchBookForm(request.GET)
    books = Book.objects.all()

    if search_form.is_valid():
        books = Book.objects.filter(title=request.GET['title'])

    return render(request, 'bookstore/books_lis.html', context={
        'books': books,
        'search_book_form': SearchBookForm,
    })


@require_http_methods(['GET', 'POST'])
def books_creation_handler(request):
    if request.method == 'GET':
        return books_create_form(request)

    return create_book(request)


def books_create_form(request):
    return render(request, 'bookstore/book_form.html', context={
        'book_form': BookForm,
    })


def create_book(request):
    form = BookForm(request.POST)
    print(request.POST)
    print(form.is_valid())

    if not form.is_valid():
        form.save()

    return redirect(reverse('all-books'))
