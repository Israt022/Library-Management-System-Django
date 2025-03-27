from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)
    ISBN = models.CharField(max_length=13)
    category = models.CharField(max_length=100)
    availability_status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Member (models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    membership_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book,related_name='borrow_books',on_delete=models.CASCADE) 
    member = models.ForeignKey(Member,related_name='borrow_books',on_delete=models.CASCADE) 
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.member.name} borrowed "{self.book.title}" on {self.borrow_date.strftime("%Y-%m-%d")}'