import django_filters
from django_filters import FilterSet

from library.models import Book


class BookFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Book
        fields = ('title',)
