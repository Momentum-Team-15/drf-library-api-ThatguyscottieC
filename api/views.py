from .models import Book, ReadingStatus
from serializers import BookSerializer, ReadingStatusSerializer, FeaturedSerializer
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import APIView
# Create your views here.


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.values_list('id', 'title', 'author')
    serializer = BookSerializer()
    permissions = (permissions.IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        return self.request.user.books.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer()


class StatusView(generics.ListAPIView):
    queryset = ReadingStatus.objects.all()
    serializer = ReadingStatusSerializer
    permissions = (permissions.IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = ReadingStatus.objects.filter(user=self.request.user)
        return queryset


class FeaturedView(generics.ListAPIView):
    queryset = Book.objects.filter(feature=True)
    serializer = FeaturedSerializer
