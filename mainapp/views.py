import json
import logging

import requests
from django import template
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from news_app.models import NewsArticle
from mainapp.models import FAQ, CompanyInfo, Coupon, Review, CompanyPrivacyPolicy, CompanySponsor, CompanyBanner
from service_app.models import Master, MasterSpeciality
from user_app.models import UserProfile

logger = logging.getLogger(__name__)


def admin_required(user):
    return user.is_authenticated and user.is_superuser


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
        'slider_delay': company_info.slider_delay_in_millis,
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
            'phone_number': entity.phone_number,
            'services': entity.speciality.services.all()
        })
    return render(request, 'mainapp/contacts.html', {'contact_list': contact_list})


def faqs(request):
    faq_list = FAQ.objects.all()
    return render(request, 'mainapp/faq/faqs.html', {'faq_list': faq_list})


def faq_page(request, faq_id):
    faq = FAQ.objects.filter(id=faq_id).first()
    return render(request, 'mainapp/faq/faq_page.html', {'data': faq})


def about(request):
    info = CompanyInfo.objects.latest('id')
    return render(request, 'mainapp/about.html', {'info': info})


def privacy_policy(request):
    latest = CompanyPrivacyPolicy.objects.latest('id')
    return render(request, 'mainapp/privacy_policy.html', {'policy': latest})


def coupons(request):
    coupon_list = Coupon.objects.filter(is_active=True)
    return render(request, 'mainapp/coupons.html', {'coupons': coupon_list})


@login_required
def reviews(request):
    user = request.user
    user_posted_review = False
    review_list = Review.objects.all()
    review_list_ext = []
    for review in review_list:
        if review.user_profile.user == user:
            user_posted_review = True
        review_list_ext.append(
            {
                'review': review,
                'full_stars': review.rating,
                'empty_stars': 5 - review.rating
            }
        )
    return render(request, 'mainapp/reviews.html', {'reviews': review_list_ext, 'review_posted': user_posted_review})


@login_required
def add_review(request):
    rating = request.POST.get('rating')
    speed_rating = request.POST.get('speed_rating')
    was_pleasant = True if request.POST.get('was_pleasant') == "on" else False
    was_clean = True if request.POST.get('was_clean') == "on" else False
    text = request.POST.get('text')
    user = request.user

    review = Review()
    review.rating = int(rating)
    review.speed_rating = speed_rating
    review.is_pleasant_master = was_pleasant
    review.is_clean_service = was_clean
    review.text = text
    review.user_profile = UserProfile.objects.filter(user=user).first()

    old_review = Review.objects.filter(user_profile__user=user)
    if old_review.exists():
        old_review_ = old_review.first()
        old_review_.rating = rating
        old_review_.text = text
        old_review_.speed_rating = review.speed_rating = speed_rating
        old_review_.is_pleasant_master = review.is_pleasant_master = was_pleasant
        old_review_.is_clean_service = review.is_clean_service = was_clean
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


@user_passes_test(admin_required)
def get_table_data(request):
    masters = User.objects.filter(groups__name='masters').all()
    contact_list = []
    specialities = MasterSpeciality.objects.all()
    for master_user in masters:
        entity = Master.objects.filter(user=master_user).get()
        contact_list.append({
            'id': entity.id,
            'name': entity.name,
            'experience': entity.experience_in_years,
            'email': master_user.email,
            'phone_number': entity.phone_number,
            'photo': entity.photo,
            'speciality': entity.speciality
        })
    return render(request, 'mainapp/management_table.html', {'contact_list': contact_list, 'specialities': specialities})


def get_master_json(request, master_id):
    master = Master.objects.filter(id=master_id).first()
    master_user = User.objects.filter(id=master.user.id).first()
    data = {
        'name': master.name,
        'experience': master.experience_in_years,
        'email': master_user.email,
        'image_url': master.photo.url,
        'phone_number': master.phone_number,
        'speciality': {
            'name': master.speciality.name,
            'description': master.speciality.description,
            'services': []
        }
    }
    for service in master.speciality.services.all():
        data['speciality']['services'].append(
            {
                'service_name': service.name,
                'service_description': service.description,
                'service_price': service.base_price_in_usd,
            }
        )
    return JsonResponse(json.dumps(data), safe=False)


@user_passes_test(admin_required)
def add_master(request):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    experience = request.POST['experience']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    avatar_url = request.POST['avatar_url']
    speciality_id = request.POST['speciality']

    new_user = User()
    new_user.email = email
    new_user.set_password('master')
    new_user.username = username
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.save()

    new_master = Master()
    new_master.user = User.objects.all().first()
    new_master.name = first_name + " " + last_name
    new_master.user = new_user
    new_master.experience_in_years = experience
    new_master.phone_number = phone_number
    new_master.speciality = MasterSpeciality.objects.filter(id=speciality_id).first()

    try:
        response = requests.get(avatar_url)
        if response.status_code == 200:
            image_content = ContentFile(response.content)
            new_master.photo.save(f"{avatar_url.split('/')[-1]}", image_content, save=True)
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred while downloading image: {e}")

    master_group = Group.objects.get(name='masters')
    master_group.user_set.add(new_user)

    new_master.save()
    return redirect('/table/')


def oop_page(request):
    return render(request, 'mainapp/oop.html')


def chart_page(request):
    return render(request, 'mainapp/chartjs.html')


@user_passes_test(admin_required)
def update_slider_setup(request):
    company_info = CompanyInfo.objects.latest('id')
    company_info.slider_delay_in_millis = request.POST['delay']
    company_info.save()
    return redirect('home')


@user_passes_test(admin_required)
def slider_setup_page(request):
    return render(request, 'mainapp/slider_setup.html')
