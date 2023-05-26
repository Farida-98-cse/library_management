from django.http import JsonResponse
from ninja import Router

from book.crud.category_crud import CategoryCRUD
from book.schema.category import CategoryIn, CategoryOut

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
