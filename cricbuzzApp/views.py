from rest_framework import generics,status

from .models import SubscriptionPlanTable, userSubscriptionTable
from .serializers import  UserSerializer, SubscriptionPlanSerializer, UserSubscriptionSerializer

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


#view to signup
@api_view(['POST'])
def userSignup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)

#view to login
@api_view(['POST'])
def userLogin(request):
    user = get_object_or_404(User, username=request.data['username'])
    
    if not user.check_password(request.data['password']):
        return Response({"error":"Invalid user"}, status=status.HTTP_404_NOT_FOUND)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

#view to get all subscription plans
@api_view(["GET"])
def getSubscriptionPlanDetails(request):
    try:
        subscriptionPlans = SubscriptionPlanTable.objects.all()
        serializer = SubscriptionPlanSerializer(subscriptionPlans, many=True)
    except:
        return Response({"error":"Failed to return data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def getSubscriptionPlanDetailsForID(request,susbscriptionID):
    try:
        subscriptionPlans = SubscriptionPlanTable.objects.get(id=susbscriptionID)
        serializer = SubscriptionPlanSerializer(subscriptionPlans)
    except:
        return Response({"error":"Failed to return data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def userSubcribed(request,susbscriptionID):
    # Get the user based on the provided authentication token
    try:
        user = Token.objects.get(key=request.auth.key).user
    except Token.DoesNotExist:
        return Response({"error": "Invalid authentication token."}, status=status.HTTP_400_BAD_REQUEST)
    except IndexError:
        return Response({"error": "Authentication token not provided."}, status=status.HTTP_400_BAD_REQUEST)

    # Get the ID value from the request body
    #id_value = request.data['subscriptionPlanID']

    # Check if a userSubscriptionTable record already exists for the user
    try:
        subscription_record = userSubscriptionTable.objects.get(user=user)
        subscription_record.subscribed.add(susbscriptionID)
        subscription_record.save()
    except userSubscriptionTable.DoesNotExist:
        # If record doesn't exist, create a new one
        subscription_record = userSubscriptionTable.objects.create(user=user)
        subscription_record.subscribed.add(susbscriptionID)

    return Response({"message":"Subscription updated successfully."}, status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getUserSubscriptions(request):
    try:
        user = Token.objects.get(key=request.auth.key).user
    except Token.DoesNotExist:
        return Response({"error": "Invalid authentication token."}, status=status.HTTP_400_BAD_REQUEST)
    except IndexError:
        return Response({"error": "Authentication token not provided."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(id=user.id)
        subscriptions = userSubscriptionTable.objects.filter(user=user)
        serializer = UserSubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"message": "User not found."}, status=404)
