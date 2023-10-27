
from django.urls import path
from .views import  userLogin,userSignup,getSubscriptionPlanDetails,getSubscriptionPlanDetailsForID

urlpatterns = [
    path('login/', userLogin, name='user-login'),
    path('signup/', userSignup, name='user-signup'),
    path('subscriptionplandetails',getSubscriptionPlanDetails, name='subscriptionPlanDetails'),
    path('subscriptionplandetail/<str:susbscriptionID>',getSubscriptionPlanDetailsForID, name='subscriptionPlanDetailForID')
]