from django.urls import path,include
from library.views import BookViewSet,AuthorViewSet,MemberViewSet,BorrowRecordViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('books',BookViewSet) 
router.register('authors',AuthorViewSet) 
router.register('members',MemberViewSet) 
router.register('borrowrecordes',BorrowRecordViewSet) 

urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

