from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DownloadSerializer, QualitySerializer
from userprofile.models import Profile
from .models import Stereo
from drf_yasg.utils import swagger_auto_schema
# Create your views here.



@api_view(['GET'])
def showQuality(request):
  try:
    profile = Profile.objects.get(id=1)
    stereo, _ = Stereo.objects.get_or_create(profile=profile)
    serializer = QualitySerializer(stereo)
    return Response(serializer.data,status=200)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)
  
@swagger_auto_schema(methods=['post'], request_body=QualitySerializer)
@api_view(['POST'])
def changeQuality(request):
  try:
    profile = Profile.objects.get(id=1)
    stereo, _ = Stereo.objects.get_or_create(profile=profile)
    serializer = QualitySerializer(stereo,data=request.data)
    if serializer.is_valid():
      serializer.save()
      print(serializer.data)
      return Response(serializer.data,status=200)
    else:
      return Response(f"{'error': {e}}", status=400)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)
  

@api_view(['GET'])
def showDownload(request):
  try:
    profile = Profile.objects.get(id=1)
    stereo, _ = Stereo.objects.get_or_create(profile=profile)
    serializer = DownloadSerializer(stereo)
    return Response(serializer.data,status=200)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)
  
@swagger_auto_schema(methods=['post'], request_body=DownloadSerializer)
@api_view(['POST'])
def changeDownload(request):
  try:
    profile = Profile.objects.get(id=1)
    stereo, _ = Stereo.objects.get_or_create(profile=profile)
    serializer = DownloadSerializer(stereo,data=request.data)
    if serializer.is_valid():
      serializer.save()
      print(serializer.data)
      return Response(serializer.data,status=200)
    else:
      return Response(f"{'error': {e}}", status=400)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)