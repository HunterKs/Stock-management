from django.contrib import admin
from .models import Company, Tyre,Customer, Status, Order, UserProfile,DailyProfit
# Register your models here.
admin.site.register(Tyre)
admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Status)
admin.site.register(Order)
admin.site.register(UserProfile)
admin.site.register(DailyProfit)