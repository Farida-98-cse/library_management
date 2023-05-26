from book.models import (
    Account
)
from django.core.exceptions import ObjectDoesNotExist


class AccountCRUD:
    @staticmethod
    def get(id: int):
        try:
            account = Account.objects.get(id=id)
            return account
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_multi():
        try:
            accounts = Account.objects.all()
            return accounts
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create(data):
        new_account = Account.objects.create(**data)
        return new_account

    @staticmethod
    def get_by_user_id(user_id):
        account = Account.objects.filter(user_id=user_id).values()


account_crud = AccountCRUD()
