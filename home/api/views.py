from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from ..models import Blog
from .serializers import BlogSerializers


class ListBlogView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    
class RetrieveBlogView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    lookup_field = "pk"
    
class UpdateBlogView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    lookup_field = "pk"
    
class DeleteBlogView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    lookup_field = "pk"

class CreateBlogView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers