from django.db.models import fields
from .models import Entry , Blog , Author
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ArticleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ("id", "headline" , "subtopics")
        