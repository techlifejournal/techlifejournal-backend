from django.db import models
from django.contrib.postgres.fields import ArrayField
from users.models import User
class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

class Entry(models.Model):
    Tags = models.ManyToManyField(Tag)
    headline = models.CharField(max_length=255,unique=True)
    content = models.TextField()
    subtopics = ArrayField(models.CharField(max_length=200))
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now_add= True)
    authors = models.ManyToManyField(User)
    number_of_comments = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    rating = models.IntegerField(default=-1)
    def __str__(self):
        return self.headline
        
