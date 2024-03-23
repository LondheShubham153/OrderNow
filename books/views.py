from django.shortcuts import render
from django.http import JsonResponse
from .models import Inventory
from django.views.decorators.csrf import csrf_exempt

import json
# Create your views/APIs here.


def health_check(request):
    return JsonResponse({"message":"the server is up"})

def get_books(request):
    results = []
    books = Inventory.objects.all()
    for book in books:
        data = {
            "title": book.title,
            "author": book.author,
            "price": book.price
        }
        results.append(data)
    return JsonResponse({"books":results})

@csrf_exempt
def add_book(request):
    data = json.loads(request.body) #convert the body to a dict
    
    book = Inventory.objects.create(
        isbn_id = data["isbn"],
        title = data["title"],
        publisher = data["publisher"],
        price = data["price"],
        quantity = data["quantity"],
        author = data["author"]
    )
    if book:
        return JsonResponse({"message":"book added successfully"})
    return JsonResponse({"message":"book not added"})