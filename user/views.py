from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import ListView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from book.models import Book, BorrowList, BorrowRecord
from django.contrib.auth.models import User
from book.views import StaffRequiredMixin, LoginRequiredMixin


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('book-list')
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('book-list')

    def form_valid(self, form):
        messages.success(self.request, 'You have been logged in.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Incorrect username or password.')
        return self.render_to_response(self.get_context_data(form=form))


class MyBorrowedBooks(LoginRequiredMixin, ListView):
    model = BorrowList
    template_name = 'user/my_books.html'
    context_object_name = 'borrow_list'

    def get_queryset(self):
        return BorrowList.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['borrow_record'] = BorrowRecord.objects.filter(
            user=self.request.user)
        return context


def UserLogoutView(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


class UserListView(StaffRequiredMixin, ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    ordering = ['username']


class UserBorrowListView(StaffRequiredMixin, ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return Book.objects.filter(borrow_list__user=user)
