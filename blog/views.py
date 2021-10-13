from rest_framework.views import APIView
from blog.models import Entry
from rest_framework import filters
from rest_framework import generics
from .serializer import (
    ArticleSerializer,
    ArticleInfoSerializer,
    CreateArticleSerializer,
)
from django.db.models.functions import Lower
from rest_framework.response import Response
from rest_framework import status
from blog.Scraper.title import gettitles
from rest_framework.permissions import BasePermission, IsAuthenticated
from users.models import User


class CreateArticle(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Entry.objects.all()

    def post(self, request, format=None):
        data = request.data
        print(data)
        try:
            titles = gettitles(data["content"])
            authour = [self.request.user.id]
            data["subtopics"] = titles
            data["Tags"] = [int(i) for i in [1]]
            data["authors"] = authour
        except Exception as e:
            print(e)
            return Response(
                {"error": "headline , content and Tags field required "},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = CreateArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticlesList(generics.ListAPIView):
    serializer_class = ArticleInfoSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["headline", "id"]
    search_fields = ["headline", "subtopics"]

    def get_queryset(self):
        queryset = Entry.objects.order_by(Lower("headline"))
        _blog = self.request.query_params.get("blog")
        _id = self.request.query_params.get("id")
        uid = self.request.query_params.get("uid")
        uname = self.request.query_params.get("uname")
        if _id is not None:
            queryset = queryset.filter(id=_id)
        if _blog is not None:
            queryset = queryset.filter(blog=_blog)
        if uid is not None:
            user = User.objects.get(id=uid)
            queryset = queryset.filter(authors=user)
        if uname is not None:
            user = User.objects.get(user_name=uname)
            queryset = queryset.filter(authors=user)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetArticle(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Entry.objects.all()
        _id = self.request.query_params.get("id")
        _blog = self.request.query_params.get("blog")
        uid = self.request.query_params.get("uid")
        uname = self.request.query_params.get("uname")
        if _id is not None:
            queryset = queryset.filter(id=_id)
        if _blog is not None:
            queryset = queryset.filter(blog=_blog)
        if uid is not None:
            user = User.objects.get(id=uid)
            queryset = queryset.filter(authors=user)
        if uname is not None:
            user = User.objects.get(user_name=uname)
            queryset = queryset.filter(authors=user)
        return queryset
