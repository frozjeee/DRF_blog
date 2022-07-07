from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import django_filters
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS, BasePermission
# Create your views here.


class PostUserWritePermission(BasePermission):
    message = "not an author"
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return  obj.author == request.user

################################################################
# class PostList(viewsets.ModelViewSet):
#     permission_classes = [PostUserWritePermission, IsAuthenticated]
#     serializer_class = PostSerializer
        
#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         print(self.kwargs)
#         return get_object_or_404(Post, slug=item)


#     def get_queryset(self):
#         slug = self.kwargs.get('pk')
#         user = self.request.user
#         return Post.objects.filter(slug=slug)
################################################################




################################################################
# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.post_objects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def create(self, request):
#         serializer_class = PostSerializer

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data) 

#     def update(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
################################################################




################################################################
class AdminPostUpload(APIView):
    permission_classes = [permissions.isAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer 

    def get_queryset(self):
        slug = self.kwargs['pk']
        print(slug) 
        return Post.objects.filter(slug=slug)


class PostDetail(generics.ListAPIView, generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer 
    

    def get_queryset(self):
        slug = self.request.query_params.get('slug')
        print(wasd)     
        return Post.objects.filter(slug=slug)


class PostListDetailFilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["^slug"]
    

class PostSearch(generics.UpdateAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
################################################################

