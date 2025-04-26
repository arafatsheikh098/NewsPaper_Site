from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_name = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

