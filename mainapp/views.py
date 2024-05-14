from django.shortcuts import render
from news_app.models import NewsArticle
from mainapp.models import FAQ


def index(request):
    latest_news = NewsArticle.objects.latest('date')
    data = {
        'latest_news': latest_news,
        'header': 'Home',
        'path': 'news/' + str(latest_news.id)
    }
    return render(request, 'mainapp/index.html', data)


def contacts(request):
    latest_news = NewsArticle.objects.latest('date')
    data = {
        'latest_news': latest_news,
        'header': 'Home',
        'path': 'news/' + str(latest_news.id)
    }
    return render(request, 'mainapp/contacts.html', data)


def faqs(request):
    faq_list = FAQ.objects.all()
    return render(request, 'mainapp/faq/faqs.html', {'faq_list': faq_list})


def about(request):
    return render(request, 'mainapp/about.html')


def privacy_policy(request):
    return render(request, 'mainapp/privacy_policy.html')

