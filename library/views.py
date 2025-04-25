from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from library.models import Book,Author,Member,BorrowRecord
from library.serializers import BookSerializer,AuthorSerializer,MemberSerializer,BorrowRecordSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsLibrarian,IsLibrarianOrReadOnly
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated,IsLibrarianOrReadOnly]

    @swagger_auto_schema(
        operation_summary="List all books",
        operation_description="List of All books.\n\nAccess by : Librarian & Members."
        )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrive a book by ID",
        operation_description= "Retrive a book by ID.\n\nAccess by : Librarian & Members. ")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new book",
        operation_description= "Create a new book.\n\nOnly Librarian can create this.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a book",
        operation_description="Update a book(full update).\n\nOnly Librarian can update books.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Partially Update a book",
        operation_description="Partially Update a book.\n\nOnly Librarian can partially update books.")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Delete a book",
        operation_description="Delete a book.\n\nOnly Librarian can Delete books.")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsLibrarian]
    
    @swagger_auto_schema(
        operation_summary="List of all Author",
        operation_description="Returns a list of all authors.\n\n Only accessible by librarians."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Retrive an Author by ID",
        operation_description="Returns details of a specific Authors.\n\n Only accessible by librarians."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="All an Author",
        operation_description="Create a new Authors.\n\n Only accessible by librarians."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Update an Author",
        operation_description="Update all field of an Authors.\n\n Only accessible by librarians."
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Partially Update an Author",
        operation_description="Update one or more fields of an author.\n\n Only accessible by librarians."
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Delete an Author",
        operation_description="Remove an Authors from Author list.\n\n Only accessible by librarians."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsLibrarian]
    
    @swagger_auto_schema(
        operation_summary="List all members",
        operation_description="Returns a list of all registered members.\n\nOnly accessible by librarians."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a member by ID",
        operation_description="Returns details of a specific member.\n\nOnly accessible by librarians."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Add a new member",
        operation_description="Register a new member in the system.\n\nOnly librarians can perform this action."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a member (full)",
        operation_description="Update all fields of a member profile.\n\nOnly librarians can perform this action."
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a member",
        operation_description="Update one or more fields of a member profile.\n\nOnly librarians can perform this action."
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a member",
        operation_description="Remove a member from the system.\n\nOnly librarians can perform this action."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class BorrowRecordViewSet(ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="List all borrow records",
        operation_description="View all borrow records.\n\nAccessible by all authenticated users."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a borrow record",
        operation_description="View details of a specific borrow record.\n\nAccessible by all authenticated users."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Borrow a book (create record)",
        operation_description="Create a borrow record to borrow a book.\n\nAccessible by authenticated users."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a borrow record (full)",
        operation_description="Update a borrow record.\n\nAccessible by authenticated users."
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update a borrow record",
        operation_description="Partially update a borrow record.\n\nAccessible by authenticated users."
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a borrow record",
        operation_description="Delete a borrow.\n\nAccessible by authenticated users."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)