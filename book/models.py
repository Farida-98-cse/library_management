from django.db import models


# Create your models here.


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

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=["name"])
        ]
