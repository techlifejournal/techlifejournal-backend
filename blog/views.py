from blog.models import Entry
from rest_framework import generics
from .serializer import ArticleSerializer 
# Create your views here.
class CreateArticle(generics.CreateAPIView):
    serializer_class = ArticleSerializer

class AllArticles(generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = ArticleSerializer
