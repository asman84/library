from rest_framework.permissions import BasePermission


class AdminGroupPermission(BasePermission):
    groups = ['admin']

    def has_permission(self, request, view):
        return (
                request.user and
                request.user.is_authenticated and
                request.user.groups.filter(name__in=self.groups).exists()
        )



class ContentGroupPermission(BasePermission):
    groups = ['content']

    def has_permission(self, request, view):
        return (
                request.user and
                request.user.is_authenticated and
                request.user.groups.filter(name__in=self.groups).exists()
        )


