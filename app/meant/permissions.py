from rest_framework.permissions import BasePermission


class AdminOnly(BasePermission):

    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return view.action in ['list', 'retrieve', 'update', 'partial_update', ] and request.user.is_superuser
