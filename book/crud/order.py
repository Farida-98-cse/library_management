from django.db import models
from django.db.models import Count
from django.db.models.functions import TruncDate

from book.models import (
    Order
)
from django.core.exceptions import ObjectDoesNotExist


class OrderCRUD:
    @staticmethod
    def get(id: int):
        try:
            order = Order.objects.get(id=id)
            return order
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_multi():
        try:
            orders = Order.objects.all()
            return orders
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create(data):
        new_order = Order.objects.create(**data)
        return new_order

    @staticmethod
    def get_recent_orders_by_book(start_date, end_date):
        count = Order.objects.filter(created_at__gte=start_date).values('book_id').\
            annotate(count_rows=models.Count('id'))
        return count

