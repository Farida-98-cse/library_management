from typing import Any, Dict, List, Optional, Union
from book.models import (
    Book
)
from django.core.exceptions import ObjectDoesNotExist


class BookCRUD:
    @staticmethod
    def get(id: int):
        try:
            book = Book.objects.get(id=id)
            return book
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_multi():
        try:
            books = Book.objects.all()
            return books
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create():
        new_book = Book.objects.create()
