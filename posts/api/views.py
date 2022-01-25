from importlib.resources import path
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django.views.decorators.csrf import csrf_exempt

from posts.models import Post
from .serializers import PostSerializer

@csrf_exempt
def post(request):
    if request.method == 'GET':
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    return HttpResponse(status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def detail(request, pk):
    if request.method == 'GET':
        queryset = Post.objects.get(id=pk)
        serializer = PostSerializer(queryset, many=False)
        return JsonResponse(serializer.data)
    return HttpResponse(status.HTTP_404_NOT_FOUND)


class HomeAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response({'detail': 'Your post was added successfully'}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response({'detail': 'Your post was updated successfully'}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
       post = Post.objects.get(id=pk)
       post.delete()
       return Response(status.HTTP_204_NO_CONTENT)