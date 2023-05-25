from django.shortcuts import render

from book.services import (
    book_service
)


def retrieve_book(request):
    books = book_service.retrieve_book()
    context = {
        "books": books
    }
    return render(request, 'books.html', context=context)
