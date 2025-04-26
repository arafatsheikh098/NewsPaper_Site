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
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.article.title}'
