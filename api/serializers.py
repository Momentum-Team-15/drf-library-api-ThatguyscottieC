from rest_framework import serializers
from .models import User, Book, ReadingStatus


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publication_date', 'featured',)


class ReadingStatusSerializer(serializers.ModelSerializer):
    class meta:
        model = ReadingStatus
        fields = ('id', 'status', 'user', 'book',)
