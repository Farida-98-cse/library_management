from ninja import Router
from django.http import JsonResponse
from django.shortcuts import render

from book.crud import BookCRUD
from book.models import Book
from book.schema.book import BookSchema, BookOut, BookIn
from book.services import (
    book_service
)


def retrieve_book(request):
    books = book_service.retrieve_book()
    context = {
        "books": books
    }
    return render(request, 'books.html', context=context)


router = Router()


@router.post('/create', response=BookOut)
def create_book(request, payload: BookIn
                ):
    try:
        data = payload.dict()
        book = BookCRUD.create(data)
        return JsonResponse({
            'book': data
        })
    except Exception as e:
        raise e