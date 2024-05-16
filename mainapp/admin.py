from django.contrib import admin

from .models import FAQ, CompanyInfo, Coupon, Review

admin.site.register(FAQ)
admin.site.register(CompanyInfo)
admin.site.register(Coupon)
admin.site.register(Review)
