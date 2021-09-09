from django.urls import path
from django.urls.conf import include 
from .views import ArticlesList, CreateArticle ,GetArticle


urlpatterns = [
    path('article/entry', CreateArticle.as_view(), name='Entry'),
    path('article/list', ArticlesList.as_view(), name='Article-List'),
     path('article/', GetArticle.as_view(), name='Articles'),
]
