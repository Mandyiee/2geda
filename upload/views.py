from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PrivacySerializer, QualitySerializer
from userprofile.models import Profile
from .models import Upload
# Create your views here.


@api_view(['GET'])
def showQuality(request):
  try:
    profile = Profile.objects.get(id=1)
    upload, _ = Upload.objects.get_or_create(profile=profile)
    serializer = QualitySerializer(upload)
    return Response(serializer.data,status=200)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)
  

@api_view(['POST'])
def changeQuality(request):
  try:
    profile = Profile.objects.get(id=1)
    upload, _ = Upload.objects.get_or_create(profile=profile)
    serializer = QualitySerializer(upload,data=request.data)
    if serializer.is_valid():
      serializer.save()
      print(serializer.data)
      return Response(serializer.data,status=200)
    else:
      return Response(f"{'error': {e}}", status=400)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)
  

@api_view(['GET'])
def showPrivacy(request):
  try:
    profile = Profile.objects.get(id=1)
    upload, _ = Upload.objects.get_or_create(profile=profile)
    serializer = PrivacySerializer(upload)
    return Response(serializer.data,status=200)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)
  

@api_view(['POST'])
def changePrivacy(request):
  try:
    profile = Profile.objects.get(id=1)
    upload, _ = Upload.objects.get_or_create(profile=profile)
    serializer = PrivacySerializer(upload,data=request.data)
    if serializer.is_valid():
      serializer.save()
      print(serializer.data)
      return Response(serializer.data,status=200)
    else:
      return Response(f"{'error': {e}}", status=400)
  except Exception as e:
    return Response(f"{'error': {e}}", status=400)