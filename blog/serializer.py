from django.db.models import fields
from .models import Entry ,Tag
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = "__all__"

class CreateArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('headline' , 'content', 'blog' , 'authors')



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class ArticleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ("id", "headline" , "subtopics")
        