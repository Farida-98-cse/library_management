from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ninja import Router

from book.crud.user_crud import CustomUserCRUD
from book.models import CustomUser
from book.schema.user import CustomUser, CustomUserSchema, CustomUserIn, CustomUserOut

router = Router()


@router.post('/create', response=CustomUserOut)
def create_category(request, payload: CustomUserIn
                    ):
    try:
        data = payload.dict()
        user = CustomUserCRUD.create(data)
        return JsonResponse({
            'user': data
        })
    except Exception as e:
        raise e
