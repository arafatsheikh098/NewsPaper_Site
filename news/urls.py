from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import signup_view

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_articles, name='category_articles'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('search/', views.search_articles, name='search_articles'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', signup_view, name='signup'),
]
