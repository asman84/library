from django.urls import path

from library.views import BookListAPIView, BookCreateAPIView, BookDeleteAPIView, LoanCreateAPIView

app_name = 'library'

urlpatterns = [
    path('book/list', BookListAPIView.as_view(),name='book-list'),
    path('book/create', BookCreateAPIView.as_view()),
    path('book/delete/<int:pk>', BookDeleteAPIView.as_view()),

    path('loan/create', LoanCreateAPIView.as_view()),
]
