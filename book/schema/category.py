from typing import Optional

from ninja import ModelSchema, Schema

from book.models import Category


class CategorySchema(ModelSchema):
    class Config:
        model = Category
        model_fields = ['name', 'limit', 'cost_per_day']


class CategoryIn(Schema):
    name: str
    limit: int
    cost_per_day: float


class CategoryOut(Schema):
    name: str
    limit: int
