from rest_framework import permissions

class IsSellerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == 'sprzedawca':
            return True
