from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from library.models import Book,Author,Member,BorrowRecord
from library.serializers import BookSerializer,AuthorSerializer,MemberSerializer,BorrowRecordSerializer

# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BorrowRecordViewSet(ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer