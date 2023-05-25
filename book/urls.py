from django.urls import path
from book.views.book import (
    retrieve_book
)

urlpatterns = [
    path("retrieve-book", retrieve_book)
]