from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsLibrarian(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'librarian'

class IsLibrarianOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.role == 'librarian'