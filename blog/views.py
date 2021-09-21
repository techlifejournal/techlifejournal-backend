from blog.models import Entry
from rest_framework import filters
from rest_framework import generics
from .serializer import ArticleSerializer , ArticleInfoSerializer , CreateArticleSerializer
from django.db.models.functions import Lower
from rest_framework.response import Response
from rest_framework import status 

class CreateArticle(generics.CreateAPIView):
    serializer_class = CreateArticleSerializer
    queryset = Entry.objects.all()


class ArticlesList(generics.ListAPIView):
    serializer_class = ArticleInfoSerializer
    filter_backends = [filters.OrderingFilter ,filters.SearchFilter]
    ordering_fields = ['headline', 'id']
    search_fields = ['headline', 'subtopics']
    def get_queryset(self):
        queryset = Entry.objects.order_by(Lower("headline"))
        _blog = self.request.query_params.get('blog')
        if _blog is not None:
            queryset = queryset.filter(blog=_blog )
        return queryset
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class GetArticle(generics.ListAPIView):
    serializer_class = ArticleSerializer
    def get_queryset(self):
        queryset = Entry.objects.all()
        _id = self.request.query_params.get('id')
        _blog = self.request.query_params.get('blog')
        if _id is not None:
            queryset = queryset.filter(id=_id )
        if _blog is not None:
            queryset = queryset.filter(blog=_blog )
        return queryset