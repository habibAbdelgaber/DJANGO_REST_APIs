from rest_framework.permissions import BasePermission

class IsPostAuthor(BasePermission):
   def has_object_permission(self, request, view, obj):
      message = 'You are not allowed to perform this action.'
      post = obj
      return post.author == request.user