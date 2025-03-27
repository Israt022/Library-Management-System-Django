from rest_framework import serializers
from library.models import Author,Book,Member,BorrowRecord

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','biography']
        
        
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer
    class Meta:
        model = Book
        fields = ['id','title','author','ISBN','category','availability_status']
        
        
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id','name','email','membership_date']
        
        
class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['id','book','member','borrow_date','return_date']
        
        