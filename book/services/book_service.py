from book.crud import BookCRUD


def retrieve_book():
    books = BookCRUD.get_multi() or []
    return books