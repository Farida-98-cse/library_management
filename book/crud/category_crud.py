from book.models import (
    Category
)
from django.core.exceptions import ObjectDoesNotExist


class CategoryCRUD:
    @staticmethod
    def get(id: int):
        try:
            category = Category.objects.get(id=id)
            return category
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_multi():
        try:
            categories = Category.objects.all()
            return categories
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create(data):
        new_category = Category.objects.create(**data)
        return new_category

    @staticmethod
    def get_by_book_id(book_id):
        category = Category.objects.filter(book_id=book_id).values()


category_crud = CategoryCRUD()
