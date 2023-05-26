from ninja import Router
from django.http import JsonResponse
from django.shortcuts import render

from book.models import Book
from book.schema.book import BookSchema, BookIn
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


@router.post('/create')
def create_book(request, payload: BookIn
                ):
    try:
        json_data = payload.dict()
        book = Book(
            name=json_data.get('name'),
            author=json_data['author'],
            borrow_inventory=json_data['borrow_inventory'],
            sell_inventory=json_data['sell_inventory'],
            sell_price=json_data['sell_price']
        )
        book.save()
        schema = BookSchema.from_django(book)

        return JsonResponse({
            'book': schema.dict()
        })
    except Exception as e:
        raise e
