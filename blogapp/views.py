from django.shortcuts import render
from rest_framework import generics
from .models import Blog
from blogapp.serializers import BlogSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
# class BlogList(generics.ListAPIView):
#     serializer_class = BlogSerializer
#     queryset = Blog.objects.all()


class BlogGRUD(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer