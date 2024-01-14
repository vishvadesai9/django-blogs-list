
from rest_framework import viewsets, pagination
from blogs_app.models import BlogPost
from blogs_app.serializers import BlogPostSerializers
# Create your views here.

class BlogsPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size=10

class BlogsView(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    pagination_class = BlogsPagination

