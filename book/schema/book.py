from typing import Optional

from ninja import ModelSchema, Schema
from book.models import Book


class BookSchema(ModelSchema):
    class Config:
        model = Book
        model_fields = ['name', 'author']


class BookIn(Schema):
    name: str
    author: str
    borrow_inventory: Optional[int]
    sell_inventory: Optional[int]
    sell_price: Optional[int]
