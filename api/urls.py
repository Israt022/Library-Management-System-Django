from django.urls import path,include
from library.views import BookViewSet,AuthorViewSet,MemberViewSet,BorrowRecordViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('books',BookViewSet) 

urlpatterns = [
    path('',include(router.urls)),
]

