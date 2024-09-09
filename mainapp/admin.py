from django.contrib import admin

from .models import FAQ, CompanyInfo, Coupon, Review, CompanyPrivacyPolicy, CompanySponsor, CompanyBanner

admin.site.register(FAQ)
admin.site.register(CompanyInfo)
admin.site.register(Coupon)
admin.site.register(Review)
admin.site.register(CompanyPrivacyPolicy)
admin.site.register(CompanySponsor)
admin.site.register(CompanyBanner)
