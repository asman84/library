from rest_framework import serializers

from library.models import Book, Loan


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'is_available', 'page_count', 'author')


class BookDetailUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'is_available', 'page_count', 'author')


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'is_available', 'page_count', 'author')


class LoanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('id', 'book', 'user')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created_at'] = instance.created_at
        data['updated_at'] = instance.updated_at
        return data
