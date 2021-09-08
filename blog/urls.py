from django.urls import path
from django.urls.conf import include 
from .views import ArticlesList, CreateArticle 


urlpatterns = [
    path('article/entry', CreateArticle.as_view(), name='Entry'),
    path('article/', ArticlesList.as_view(), name='Articles'),
]
