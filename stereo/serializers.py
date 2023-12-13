from rest_framework import serializers
from .models import Stereo

class QualitySerializer(serializers.ModelSerializer):
  class Meta:
    model = Stereo
    fields = ['quality']
    
class DownloadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Stereo
    fields = ['offlineDownload']
    
