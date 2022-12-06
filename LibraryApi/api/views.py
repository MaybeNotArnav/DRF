from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bookshelf(request):
    book =Book.objects.all()
    serializer = BookSerializer(book,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def book_read(request,title):
    try:
        book = Book.objects.get(title=title)
    except Book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
        
@api_view(['PUT'])
def book_update(request,title):
    try:
        book = Book.objects.get(title=title)
    except Book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def book_delete(request,title):
    try:
        book = Book.objects.get(title=title)
    except Book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
