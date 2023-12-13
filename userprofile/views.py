from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProfileSerializer
from .models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

@api_view(['GET'])
def showProfile(request):
  try:
    user = User.objects.get(id=1)
    profile, _ = Profile.objects.get_or_create(user=user)
    print(profile)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data, status=201)
  except Exception as e:
   return Response(f"{'error': {e}}", status=400)

@swagger_auto_schema(methods=['post'], request_body=ProfileSerializer)
@api_view(['POST'])
def createProfile(request):
  user, _ = User.objects.get_or_create(id=1)
  if Profile.objects.filter(user=user).exists():
    return Response("{'error': 'profile already exists'}", status=400)
  serializer = ProfileSerializer(data=request.POST)
  if serializer.is_valid():
    serializer.save(user=user)
    return Response(serializer.data, status=201)
  return Response(serializer.errors, status=400)

@swagger_auto_schema(methods=['put'], request_body=ProfileSerializer)
@api_view(['PUT'])
def changeProfile(request):
  try:
    profile = Profile.objects.get(id=1)
  except Profile.DoesNotExist:
    return Response("{'error':'Profile does not exist'}", status=400)
  serializer = ProfileSerializer(profile,data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=201)
  return Response(serializer.errors, status=400)