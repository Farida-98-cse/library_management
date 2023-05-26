from typing import Optional

from ninja import ModelSchema, Schema

from book.models import CustomUser


class CustomUserSchema(ModelSchema):
    class Config:
        model = CustomUser
        model_fields = ['role', 'national_id']


class CustomUserIn(Schema):
    national_id: str
    role: str
    password: float


class CustomUserOut(Schema):
    national_id: str
    role: str
