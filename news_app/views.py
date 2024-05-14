from django.shortcuts import render
from .models import NewsArticle


def news_method(request):
    news = NewsArticle.objects.order_by('-date')
    return render(request, 'news_app/index.html', {'news': news})


def news_article_page(request, article_id):
    news = NewsArticle.objects.get(pk=article_id)
    return render(request, 'news_app/news_article_layout.html', {'news': news})
