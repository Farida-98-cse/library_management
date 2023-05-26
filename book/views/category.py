from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ninja import Router

from book.crud.category_crud import CategoryCRUD
from book.models import Category
from book.schema.category import CategoryIn, CategoryOut, CategorySetBook

router = Router()


@router.post('/create', response=CategoryOut)
def create_category(request, payload: CategoryIn
                    ):
    try:
        data = payload.dict()
        book = CategoryCRUD.create(data)
        return JsonResponse({
            'category': data
        })
    except Exception as e:
        raise e


@router.put('/book-to-category/{category_id}')
def assign_book_to_category(request, category_id: int, payload: CategorySetBook):
    try:
        category = get_object_or_404(Category, id=category_id)
        for attr, value in payload.dict().items():
            setattr(category, attr, value)
        category.save()
        return {"success": True}
    except Exception as e:
        raise e
