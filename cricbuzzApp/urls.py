
from django.urls import path
from .views import  getUserSubscriptions, userLogin,userSignup,getSubscriptionPlanDetails,getSubscriptionPlanDetailsForID,userSubcribed

urlpatterns = [
    path('login/', userLogin, name='user-login'),
    path('signup/', userSignup, name='user-signup'),
    path('subscriptionplandetails',getSubscriptionPlanDetails, name='subscriptionPlanDetails'),
    path('subscriptionplandetail/<str:susbscriptionID>',getSubscriptionPlanDetailsForID, name='subscriptionPlanDetailForID'),
    path('usersubcribed/<str:susbscriptionID>',userSubcribed, name="userSubscribed"),
    path('user',getUserSubscriptions, name='subscriptionPlanDetailForuserID')
]