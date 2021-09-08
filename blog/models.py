from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.name
class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255,unique=True)
    content = models.TextField()
    subtopics = models.TextField(default="")
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now_add= True)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    rating = models.IntegerField()
    def __str__(self):
        return self.headline
        
