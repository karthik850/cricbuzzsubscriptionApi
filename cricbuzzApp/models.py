from typing_extensions import Required
from django.db import models
from tinymce.models import HTMLField



class SubscriptionPlanTable(models.Model):
    planName = models.CharField(max_length=100);
    planDescription = models.CharField(max_length=100)
    planAmount = models.FloatField()
    planDiscountName = models.CharField(max_length=100,blank=True)
    planDiscountPercentage = models.FloatField(null=True,blank=True) 

    def __str__(self):
        return self.planName

class BenefitsTable(models.Model):
    selectedPlan = models.ManyToManyField(SubscriptionPlanTable, related_name="selectedPlan")
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    imageUrl = models.URLField(blank=True)
    specialBenfit= models.BooleanField(default=False)
    iconName=models.CharField(max_length=100, blank=True)
    fullDetails = HTMLField(blank=True)

    def __str__(self):
        return self.Name
    
