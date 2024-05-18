from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView, name='logout'),
    path('my-books/', views.MyBorrowedBooks.as_view(), name='my-books'),
    path('students/', views.UserListView.as_view(), name='student-list'),
    path('student/<int:pk>/', views.UserBorrowListView.as_view(), name='student-borrow-list'),
]