from django.shortcuts import render,redirect
from .models import Book
from .serializers import BookSerializer
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(wait)
    context = {'form':form}
    return render(request,'signup.html',context)

def wait (request):
    return render(request,'wait.html')

def confirmation(request,token):
    token_del = Token.objects.get(key=token)
    user_id = token_del.user_id
    print(user_id)
    user = User.objects.get(id=user_id)
    print(user)
    user.is_active=True
    token_del.delete()
    user.save()
    return render(request,'confirm.html',{'user':user.username})


@api_view(['GET'])
def bookshelf(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def book_read(request, title):
    try:
        book = Book.objects.get(title=title)
    except Book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)


@api_view(['PUT'])
def book_update(request, title):
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
def book_delete(request, title):
    try:
        book = Book.objects.get(title=title)
    except Book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
