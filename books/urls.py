from django.urls import path
from .views import health_check,get_books,add_book

urlpatterns = [
    path('health/', health_check),
    path('list/',get_books),
    path('add/',add_book)
]
