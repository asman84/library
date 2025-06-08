from django.db import models

from accounts.models import User
from toolkit.models import BaseModel


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)


class Book(models.Model):
    title = models.CharField(max_length=10)
    isbn = models.CharField(max_length=30, default="123")
    is_available = models.BooleanField(default=True)
    page_count = models.IntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)


class Loan(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

