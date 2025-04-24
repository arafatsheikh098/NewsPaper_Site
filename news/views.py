from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.db.models import Q 

def home(request):
    query = request.GET.get('q')  # q is the input name in our form
    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by('-date_posted')
    else:
        articles = Article.objects.all().order_by('-date_posted')[:5] 
    categories = Category.objects.all()
    return render(request, 'home.html', {'articles': articles, 'categories': categories, 'query': query})

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


def search_articles(request):
    query = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=query) if query else []
    return render(request, 'search_results.html', {'articles': articles, 'query': query})
