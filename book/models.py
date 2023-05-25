from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from enum import Enum


class Role(Enum):
    staff = 'Staff'
    member = 'Member'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class BookStatus(Enum):
    checkout = 'CheckOut'
    hold = 'Hold'
    sold = 'Soled'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Book(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    borrow_inventory = models.IntegerField(default=5)
    sell_inventory = models.IntegerField(default=5)
    sell_price = models.FloatField(default=10.0)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=["name"])
        ]


class Category(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    limit = models.IntegerField(default=5)
    cost_per_day = models.FloatField(default=10.0)
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books', null=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=["name"])
        ]


class CustomUser(AbstractBaseUser):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    national_id = models.CharField(max_length=20, blank=True, default="")
    role = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in Role], default=Role.member)

    def __str__(self):
        return self.national_id


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    is_returned = models.BooleanField()
    return_date = models.DateField(null=True)
    status = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in BookStatus],
                              default=BookStatus.sold)
