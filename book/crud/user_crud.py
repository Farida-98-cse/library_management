from book.models import (
    CustomUser
)
from django.core.exceptions import ObjectDoesNotExist


class CustomUserCRUD:
    @staticmethod
    def get(id: int):
        try:
            user = CustomUser.objects.get(id=id)
            return user
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_multi():
        try:
            users = CustomUser.objects.all()
            return users
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create(data):
        new_user = CustomUser.objects.create(**data)
        return new_user
