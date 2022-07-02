from django import forms
from bookstore.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'description',
            'published_at',
            'author_id'
        ]
        widgets = {
            'published_at': forms.DateInput(
                format='%m/%d/%Y',
                attrs={
                    'class': 'form-control', 'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }


class SearchBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
        ]