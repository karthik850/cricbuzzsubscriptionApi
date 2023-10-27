from django.contrib import admin

from .models import BenefitsTable, SubscriptionPlanTable
# Register your models here.
admin.site.register(SubscriptionPlanTable)
admin.site.register(BenefitsTable)