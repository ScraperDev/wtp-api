from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom Permission that allows only the owners of an object to edit that object.
    """

    def has_object_permission(self, request, view, obj):
        # If GET / HEAD / OPTIONS
        if request.method in SAFE_METHODS:
            return True
        # Else check if the owner of the object is the user.
        return obj.owner == request.user