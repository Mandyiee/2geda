from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AudioSerializer,VideoSerializer
from userprofile.models import Profile
from .models import Livestreaming
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


@api_view(['GET'])
def showAudio(request):
  try:
    profile = Profile.objects.get(id=1)
    livestreaming, _ = Livestreaming.objects.get_or_create(profile=profile)
    serializer = AudioSerializer(livestreaming)
    return Response(serializer.data,status=200)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)
  
@swagger_auto_schema(methods=['post'], request_body=AudioSerializer)
@api_view(['POST'])
def changeAudio(request):
  try:
    profile = Profile.objects.get(id=1)
    livestreaming, _ = Livestreaming.objects.get_or_create(profile=profile)
    serializer = AudioSerializer(livestreaming,data=request.data)
    if serializer.is_valid():
      serializer.save()
      print(serializer.data)
      return Response(serializer.data,status=200)
    else:
      return Response(f"{'error': {e}}", status=400)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)
  
  
@api_view(['GET'])
def showVideo(request):
  try:
    profile = Profile.objects.get(id=1)
    livestreaming, _ = Livestreaming.objects.get_or_create(profile=profile)
    serializer = VideoSerializer(livestreaming)
    return Response(serializer.data,status=200)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)
  
@swagger_auto_schema(methods=['post'], request_body=VideoSerializer)
@api_view(['POST'])
def changeVideo(request):
  try:
    profile = Profile.objects.get(id=1)
    livestreaming, _ = Livestreaming.objects.get_or_create(profile=profile)
    serializer = VideoSerializer(livestreaming,data=request.data)
    if serializer.is_valid():
      serializer.save()
      print(serializer.data)
      return Response(serializer.data,status=200)
    else:
      return Response(f"{'error': {e}}", status=400)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)