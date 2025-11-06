from rest_framework import serializers
from .models import Book, Category, AccessRequest


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'category', 'category_name', 
                  'cover', 'access_type', 'downloads', 'created_at', 'updated_at']


class AccessRequestSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    book_title = serializers.CharField(source='book.title', read_only=True)
    
    class Meta:
        model = AccessRequest
        fields = ['id', 'user', 'user_username', 'book', 'book_title', 'status', 
                  'message', 'created_at', 'reviewed_at']
        read_only_fields = ['status', 'reviewed_at']
