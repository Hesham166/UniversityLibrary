from .models import BorrowList, BorrowRecord
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Book, Author, Category, Publisher
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views import View
from datetime import datetime


def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'book/home.html', context)


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        raise PermissionDenied


################ Book Views ################

class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'
    ordering = ['title']


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_borrow = BorrowList.objects.filter(
            user=self.request.user, book=self.object).exists()
        context['user_borrow'] = user_borrow
        return context


class BookCreateView(StaffRequiredMixin, CreateView):
    model = Book
    template_name = 'book/book_form.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        messages.success(self.request, 'Book added successfully.')
        return super().form_valid(form)


class BookUpdateView(StaffRequiredMixin, UpdateView):
    model = Book
    template_name = 'book/book_form.html'
    fields = '__all__'
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        messages.success(self.request, 'Book updated successfully.')
        return super().form_valid(form)


class BookDeleteView(StaffRequiredMixin, DeleteView):
    model = Book
    template_name = 'book/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        messages.success(self.request, 'Book deleted successfully.')
        return super().form_valid(form)


class BorrowView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=self.kwargs['pk'])
        if BorrowList.objects.filter(user=self.request.user, book=book).exists():
            messages.error(request, 'You have already borrowed this book.')
        else:
            BorrowList.objects.create(user=self.request.user, book=book)
            messages.success(
                request, 'You have borrowed the book successfully.')
        return redirect('book-detail', pk=book.pk)


class ReturnView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=self.kwargs['pk'])
        borrow_list = BorrowList.objects.filter(
            user=self.request.user, book=book)
        if not borrow_list.exists():
            messages.error(request, 'You have not borrowed this book.')
        else:
            borrow_record = BorrowRecord.objects.create(
                user=self.request.user, book=book, borrow_date=borrow_list[0].borrow_date)
            borrow_record.return_date = datetime.now().strftime('%Y-%m-%d')
            borrow_record.save()
            borrow_list.delete()
            messages.success(
                request, 'You have returned the book successfully.')
        return redirect('book-detail', pk=book.pk)

################ Author Views ################


class AuthorBookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        author = get_object_or_404(Author, pk=self.kwargs.get('pk'))
        return Book.objects.filter(author=author)


class AuthorListView(ListView):
    model = Author
    template_name = 'book/author_list.html'
    context_object_name = 'authors'
    ordering = ['name']


class AuthorCreateView(StaffRequiredMixin, CreateView):
    model = Author
    template_name = 'book/author_form.html'
    fields = '__all__'
    success_url = reverse_lazy('author-list')

    def form_valid(self, form):
        messages.success(self.request, 'Author added successfully.')
        return super().form_valid(form)


class AuthorUpdateView(StaffRequiredMixin, UpdateView):
    model = Author
    template_name = 'book/author_form.html'
    fields = '__all__'
    success_url = reverse_lazy('author-list')

    def form_valid(self, form):
        messages.success(self.request, 'Author updated successfully.')
        return super().form_valid(form)


class AuthorDeleteView(StaffRequiredMixin, DeleteView):
    model = Author
    template_name = 'book/author_confirm_delete.html'
    success_url = reverse_lazy('author-list')

    def form_valid(self, form):
        messages.success(self.request, 'Author deleted successfully.')
        return super().form_valid(form)


################ Category Views ################


class CategoryBookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return Book.objects.filter(category=category)


class CategoryListView(ListView):
    model = Category
    template_name = 'book/category_list.html'
    context_object_name = 'categories'
    ordering = ['name']


class CategoryCreateView(StaffRequiredMixin, CreateView):
    model = Category
    template_name = 'book/category_form.html'
    fields = '__all__'
    success_url = reverse_lazy('category-list')

    def form_valid(self, form):
        messages.success(self.request, 'Category added successfully.')
        return super().form_valid(form)


class CategoryUpdateView(StaffRequiredMixin, UpdateView):
    model = Category
    template_name = 'book/category_form.html'
    fields = '__all__'
    success_url = reverse_lazy('category-list')

    def form_valid(self, form):
        messages.success(self.request, 'Category updated successfully.')
        return super().form_valid(form)


class CategoryDeleteView(StaffRequiredMixin, DeleteView):
    model = Category
    template_name = 'book/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')

    def form_valid(self, form):
        messages.success(self.request, 'Category deleted successfully.')
        return super().form_valid(form)


################ Publisher Views ################


class PublisherBookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        publisher = get_object_or_404(Publisher, pk=self.kwargs.get('pk'))
        return Book.objects.filter(publisher=publisher)


class PublisherListView(ListView):
    model = Publisher
    template_name = 'book/publisher_list.html'
    context_object_name = 'publishers'
    ordering = ['name']


class PublisherCreateView(StaffRequiredMixin, CreateView):
    model = Publisher
    template_name = 'book/publisher_form.html'
    fields = '__all__'
    success_url = reverse_lazy('publisher-list')

    def form_valid(self, form):
        messages.success(self.request, 'Publisher added successfully.')
        return super().form_valid(form)


class PublisherUpdateView(StaffRequiredMixin, UpdateView):
    model = Publisher
    template_name = 'book/publisher_form.html'
    fields = '__all__'
    success_url = reverse_lazy('publisher-list')

    def form_valid(self, form):
        messages.success(self.request, 'Publisher updated successfully.')
        return super().form_valid(form)


class PublisherDeleteView(StaffRequiredMixin, DeleteView):
    model = Publisher
    template_name = 'book/publisher_confirm_delete.html'
    success_url = reverse_lazy('publisher-list')

    def form_valid(self, form):
        messages.success(self.request, 'Publisher deleted successfully.')
        return super().form_valid(form)
