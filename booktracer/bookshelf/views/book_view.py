from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from booktracer.bookshelf.models.books import Book


class BookView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except  Book.DoesNotExist:
            return  Response({'error':'Book not Found'}, status = status.HTTP_404_NOT_FOUND)
