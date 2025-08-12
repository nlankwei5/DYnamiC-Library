from rest_framework import permissions


class isUploaderOrReadOnly(permissions.BasePermission):
    
    def has_uploader_permissions (self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True 

        return obj.uploader == request.user     
