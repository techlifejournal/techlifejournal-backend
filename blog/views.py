from blog.models import Entry
from rest_framework import filters
from rest_framework import generics
from .serializer import ArticleSerializer , ArticleInfoSerializer
from django.db.models.functions import Lower
from rest_framework.response import Response
import django_filters.rest_framework
from rest_framework import status 
from django.contrib.postgres.search import SearchVector
# Create your views here.
class CreateArticle(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ArticlesList(generics.ListAPIView):
    queryset = Entry.objects.order_by(Lower("headline"))
    serializer_class = ArticleInfoSerializer
    filter_backends = [filters.OrderingFilter ,filters.SearchFilter]
    ordering_fields = ['headlines', 'id']
    search_fields = ['headline', 'subtopics']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

