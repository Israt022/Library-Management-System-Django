from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from library.models import Book,Author,Member,BorrowRecord
from library.serializers import BookSerializer,AuthorSerializer,MemberSerializer,BorrowRecordSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsLibrarian,IsLibrarianOrReadOnly

# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated,IsLibrarianOrReadOnly]

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsLibrarian]
    
    
class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsLibrarian]

class BorrowRecordViewSet(ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAuthenticated]