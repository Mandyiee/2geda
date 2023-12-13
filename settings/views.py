from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MyFeedSerializer, OtherFeedSerializer, TaggingSerializer
from userprofile.models import Profile
from .models import Settings
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

@api_view(['GET'])
def showMyFeed(request):
  try:
    profile = Profile.objects.get(id=1)
    setting, _ = Settings.objects.get_or_create(profile=profile)
    serializer = MyFeedSerializer(setting)
    return Response(serializer.data,status=200)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)
  
@api_view(['GET'])
def showOtherFeed(request):
  try:
    profile = Profile.objects.get(id=1)
    setting, _ = Settings.objects.get_or_create(profile=profile)
    serializer = OtherFeedSerializer(setting)
    return Response(serializer.data,status=200)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)
  
@api_view(['GET'])
def showTagging(request):
  try:
    profile = Profile.objects.get(id=1)
    setting, _ = Settings.objects.get_or_create(profile=profile)
    serializer = TaggingSerializer(setting)
    return Response(serializer.data,status=200)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)
    
@swagger_auto_schema(methods=['post'], request_body=MyFeedSerializer)
@api_view(['POST'])
def changeMyFeed(request):
  try:
    profile = Profile.objects.get(id=1)
    setting, _ = Settings.objects.get_or_create(profile=profile)
    serializer = MyFeedSerializer(setting,data=request.data)
    if serializer.is_valid():
      serializer.save()
      print(serializer.data)
      return Response(serializer.data,status=200)
    else:
      return Response(f"{'error': {e}}", status=400)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)
  
@swagger_auto_schema(methods=['post'], request_body=OtherFeedSerializer)
@api_view(['POST'])
def changeOtherFeed(request):
  try:
    profile = Profile.objects.get(id=1)
    setting, _ = Settings.objects.get_or_create(profile=profile)
    serializer = OtherFeedSerializer(setting,data=request.data)
    if serializer.is_valid():
      serializer.save()
      print(serializer.data)
      return Response(serializer.data,status=200)
    else:
      return Response(f"{'error': {e}}", status=400)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)

@swagger_auto_schema(methods=['post'], request_body=TaggingSerializer)
@api_view(['POST'])
def changeTagging(request):
  try:
    profile = Profile.objects.get(id=1)
    setting, _ = Settings.objects.get_or_create(profile=profile)
    serializer = TaggingSerializer(setting,data=request.data)
    if serializer.is_valid():
      serializer.save()
      print(serializer.data)
      return Response(serializer.data,status=200)
    else:
      return Response(f"{'error': {e}}", status=400)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)