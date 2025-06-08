from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.permissions import AdminGroupPermission
from library.filters import BookFilter
from library.models import Book
from library.serializers import BookListSerializer, BookDetailUpdateSerializer, BookCreateSerializer, \
    LoanCreateSerializer


# Create your views here.
class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    permission_classes = [AllowAny]
    filterset_class = BookFilter



    def get_permissions(self):
        if self.request.query_params:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()




class BookCreateAPIView(generics.CreateAPIView):
    serializer_class = BookCreateSerializer
    permission_classes = [AdminGroupPermission]

class BookDeleteAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [AdminGroupPermission]


class LoanCreateAPIView(generics.CreateAPIView):
    serializer_class = LoanCreateSerializer
    permission_classes = [AdminGroupPermission]
