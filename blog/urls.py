from django.urls import path
from django.urls.conf import include 
from .views import AllArticlesList, CreateArticle 


urlpatterns = [
    path('article/', CreateArticle.as_view(), name='Entry'),
    path('article/all/', AllArticlesList.as_view(), name='Articles')
]
