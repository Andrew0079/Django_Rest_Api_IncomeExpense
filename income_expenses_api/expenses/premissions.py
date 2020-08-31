from rest_framework import permissions

# checking if user has permission to do CRUD operations


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
