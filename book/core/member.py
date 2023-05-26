from book.crud import account_crud


class Member:
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    @staticmethod
    def check_account_inventory(self, user_id):
        account = account_crud.get_by_user_id(user_id)
        return account
