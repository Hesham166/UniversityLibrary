from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/add/', views.BookCreateView.as_view(), name='book-add'),
    path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),
    path('books/borrow/<int:pk>/', views.BorrowView.as_view(), name='book-borrow'),
    path('books/return/<int:pk>/', views.ReturnView.as_view(), name='book-return'),
    path('authors/<int:pk>/', views.AuthorBookListView.as_view(), name='author-books'),
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('authors/add/', views.AuthorCreateView.as_view(), name='author-add'),
    path('authors/update/<int:pk>/', views.AuthorUpdateView.as_view(), name='author-update'),
    path('authors/delete/<int:pk>/', views.AuthorDeleteView.as_view(), name='author-delete'),
    path('categories/<int:pk>/', views.CategoryBookListView.as_view(), name='category-books'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category-add'),
    path('categories/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('categories/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('publishers/<int:pk>/', views.PublisherBookListView.as_view(), name='publisher-books'),
    path('publishers/', views.PublisherListView.as_view(), name='publisher-list'),
    path('publishers/add/', views.PublisherCreateView.as_view(), name='publisher-add'),
    path('publishers/update/<int:pk>/', views.PublisherUpdateView.as_view(), name='publisher-update'),
    path('publishers/delete/<int:pk>/', views.PublisherDeleteView.as_view(), name='publisher-delete'),
]