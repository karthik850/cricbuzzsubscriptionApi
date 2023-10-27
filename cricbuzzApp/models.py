from typing_extensions import Required
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


#holds all subcription details
class SubscriptionPlanTable(models.Model):
    planName = models.CharField(max_length=100);
    planDescription = models.CharField(max_length=100)
    planAmount = models.FloatField()
    planDiscountName = models.CharField(max_length=100,blank=True)
    planDiscountPercentage = models.FloatField(null=True,blank=True) 

    def __str__(self):
        return self.planName

#holds benefitsdetails
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

#holds usersubcription details  
class userSubscriptionTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="student")
    subscribed = models.ManyToManyField(SubscriptionPlanTable, related_name="subscribed")



    
