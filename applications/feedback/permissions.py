from rest_framework.permissions import BasePermission


class IsAuthenticatedOrIsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ('PUT', 'PATCH', 'DELETE'):
            return request.user.is_owner
        return request.user.is_authenticated == request.user.is_staff
