from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Book
from .serializers import BookSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

# Create your views here.


@csrf_exempt
def bookshelf(request):
    if request.method == 'GET':
        book =Book.objects.all()
        serializer = BookSerializer(book,many=True)
        return JsonResponse(serializer.data,safe =False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def book_read(request,title):
    try:
        book = Book.objects.get(title=title)
    except Book.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)
        
    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)