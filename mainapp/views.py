import json
import logging

import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from news_app.models import NewsArticle
from mainapp.models import FAQ, CompanyInfo, Coupon, Review, CompanyPrivacyPolicy, CompanySponsor, CompanyBanner
from service_app.models import Master
from user_app.models import UserProfile

logger = logging.getLogger(__name__)


def index(request):
    latest_news = NewsArticle.objects.latest('date')
    company_info = CompanyInfo.objects.latest('id')
    sponsors = CompanySponsor.objects.all()
    banners = CompanyBanner.objects.all()
    data = {
        'latest_news': latest_news,
        'header': 'Home',
        'path': 'news/' + str(latest_news.id),
        'joke': random_joke(request),
        'cat_fact': random_cat_fact(request),
        'logo': company_info.logo,
        'sponsors': sponsors,
        'banners': banners
    }
    return render(request, 'mainapp/index.html', data)


def contacts(request):
    masters = User.objects.filter(groups__name='masters').all()
    contact_list = []
    for master_user in masters:
        entity = Master.objects.filter(user=master_user).get()
        contact_list.append({
            'name': entity.name,
            'experience': entity.experience_in_years,
            'email': master_user.email,
            'photo': entity.photo,
            'services': entity.speciality.services.all()
        })
    return render(request, 'mainapp/contacts.html', {'contact_list': contact_list})


def faqs(request):
    faq_list = FAQ.objects.all()
    return render(request, 'mainapp/faq/faqs.html', {'faq_list': faq_list})


def about(request):
    info = CompanyInfo.objects.latest('id')
    return render(request, 'mainapp/about.html', {'info': info})


def privacy_policy(request):
    latest = CompanyPrivacyPolicy.objects.latest('id')
    return render(request, 'mainapp/privacy_policy.html', {'policy': latest})


def coupons(request):
    coupon_list = Coupon.objects.filter(is_active=True)
    return render(request, 'mainapp/coupons.html', {'coupons': coupon_list})


def reviews(request):
    review_list = Review.objects.all()
    return render(request, 'mainapp/reviews.html', {'reviews': review_list})


@login_required
def add_review(request):
    rating = request.POST.get('rating')
    text = request.POST.get('text')
    user = request.user
    review = Review()
    review.rating = int(rating)
    review.text = text
    review.user_profile = UserProfile.objects.filter(user=user).first()

    old_review = Review.objects.filter(user_profile__user=user)
    if old_review.exists():
        old_review_ = old_review.first()
        old_review_.rating = rating
        old_review_.text = text
        old_review_.user_profile = review.user_profile
        old_review_.save()
    else:
        review.save()
    logger.info(f"Review of user {user.username} successfully added")
    return redirect('/review/')


def random_joke(request):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()
    return dict(data)


def random_cat_fact(request):
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    return dict(data)
