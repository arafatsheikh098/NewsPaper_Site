from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def home(request):
    articles = Article.objects.all().order_by('-date_posted')
    categories = Category.objects.all()
    return render(request, 'home.html', {'articles': articles, 'categories': categories})

def category_articles(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category).order_by('-date_posted')
    categories = Category.objects.all()
    return render(request, 'category_articles.html', {
        'category': category,
        'articles': articles,
        'categories': categories
    })
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article': article})