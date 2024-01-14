from rest_framework import serializers
from blogs_app.models import BlogPost

class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content','author', 'publication_date']