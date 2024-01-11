from rest_framework import permissions

class IsAdminOrWarden(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_roles in ['ADMIN', 'WARDEN']

class IsAdminOrWardenOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.user_roles in ['ADMIN', 'WARDEN'] or obj.user == request.user
