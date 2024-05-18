from django.db import models
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    isbn = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='books')
    publish_date = models.DateField()
    edition = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    

class BorrowList(models.Model): # current borrowed books
    book = models.ForeignKey(Book, related_name='borrow_list', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='borrow_list', on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.title} - {self.user.username}'
    

# model tha save record of all book borrows
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, related_name='borrow_records', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='borrow_records', on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.title} - {self.user.username}'