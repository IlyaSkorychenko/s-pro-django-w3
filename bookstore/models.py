from django.core.validators import MinValueValidator
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(1)])


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    published_at = models.DateField()
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

