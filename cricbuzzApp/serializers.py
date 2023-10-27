from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
import json

from .models import BenefitsTable, SubscriptionPlanTable


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password']


# class BenefitSerializer(serializers.ModelSerializer):
#       # Nest the AuthorSerializer for the ForeignKey field

#     class Meta:
#         model = BenefitsTable
#         fields = "__all__"

# class subscriptionPlanDetailsSerializer(serializers.ModelSerializer):
#     selectedPlan = BenefitSerializer(many=True, source='selectedPlan.benefits')
#     class Meta:
#         model = SubscriptionPlanTable
#         fields = "__all__"
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         benefitData = representation.pop('selectedPlan')
#         for key, value in benefitData.items():
#             representation[key] = value
#         return representation


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
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        benefit_data = representation.pop('benefits')
        
        # Convert list of benefits and concat to subscription data
        representation['benefits'] = benefit_data

        return representation

