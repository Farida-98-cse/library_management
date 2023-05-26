from book.crud import book_crud
from book.crud.category_crud import category_crud


class Book:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def check_book_hold_inventory(book_id):
        category = category_crud.get_by_book_id(book_id=book_id)
        if category:
            return category.limit

    @staticmethod
    def check_hold_days_count(self, book_id):
        n = self.check_book_hold_inventory(book_id)  # inventory of the book
        
