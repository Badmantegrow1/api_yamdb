from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from reviews.models import Category, Genre, Review, Title, User
from django.db import models


class CategoryViewSet(viewsets.ModelViewSet):
    '''Представление списка категорий.'''
    queryset = Category.objects.all()
    #serializer_class = 
    #permission_classes = 



class GenreViewSet(models.Model):
    '''Представление списка жанров.'''
    queryset = Genre.objects.all()
    #serializer_class = 
    #permission_classes =


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    #serializer_class = 
    #permission_classes =


class CommentViewSet(viewsets.ModelViewSet):
    #serializer_class = 
    #permission_classes =
    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get("review_id"))
        return review.comments.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id, title=title_id)
        serializer.save(author=self.request.user, review=review)


class ReviewViewSet(viewsets.ModelViewSet):
    #serializer_class = 
    #permission_classes =
    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get("title_id"))

        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title=title)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    #serializer_class =
    #permission_classes =
