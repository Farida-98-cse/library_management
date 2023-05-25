from django.urls import path
from django.contrib import admin
from book.views.book import (
    retrieve_book
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("retrieve-book", retrieve_book)
]
