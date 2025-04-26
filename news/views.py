from django.shortcuts import redirect, render, get_object_or_404
from .models import Article, Category
from django.db.models import Q 
from django.utils import timezone
from .forms import CommentForm

def home(request):
    query = request.GET.get('q')  # q is the input name in our form
    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by('-date_posted')
    else:
        articles = Article.objects.all().order_by('-date_posted')[:5] 
    categories = Category.objects.all()
    return render(request, 'home.html', {'articles': articles, 'categories': categories,'now': timezone.now(), 'query': query})

def category_articles(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category).order_by('-date_posted')
    categories = Category.objects.all()
    return render(request, 'category_articles.html', {
        'category': category,
        'articles': articles,
        'categories': categories,
        'now': timezone.now(),
    })
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = CommentForm()
    return render(request, 'article_detail.html', {'article': article,'now': timezone.now(),'comments': comments,
        'form': form})


def search_articles(request):
    query = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=query) if query else []
    return render(request, 'search_results.html', {'articles': articles, 'query': query})
