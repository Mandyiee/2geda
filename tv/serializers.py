from rest_framework import serializers
from .models import Tv

class TvQualitySerializer(serializers.ModelSerializer):
  class Meta:
    model = Tv
    fields = ['quality']
    
class TvDownloadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tv
    fields = ['offlineDownload']
    