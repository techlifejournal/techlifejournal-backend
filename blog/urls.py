from django.urls import path
from django.urls.conf import include 
from .views import CreateArticle , AllArticles


urlpatterns = [
    path('article/', CreateArticle.as_view(), name='Entry'),
    path('article/all/', AllArticles.as_view(), name='Articles')
]
