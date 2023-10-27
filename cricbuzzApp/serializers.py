from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
import json

from .models import BenefitsTable, SubscriptionPlanTable, userSubscriptionTable


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password']

class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenefitsTable
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(BenefitSerializer, self).__init__(*args, **kwargs)
        # Exclude the field you want to exclude
        excluded_field = 'selectedPlan'  
        if excluded_field in self.fields:
            del self.fields[excluded_field]

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    benefits = BenefitSerializer(many=True, source='selectedPlan')

    class Meta:
        model = SubscriptionPlanTable
        fields = '__all__'
    #to control representation
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        benefit_data = representation.pop('benefits')
        # Convert list of benefits and concat to subscription data
        representation['benefits'] = benefit_data
        return representation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']  

class UserSubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlanTable
        fields = ['planName']

class UserSubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer()  
    subscribed = UserSubscriptionPlanSerializer(many=True)  

    class Meta:
        model = userSubscriptionTable
        fields = ['user', 'subscribed'] 

