from rest_framework import serializers
from .models import Upload

class QualitySerializer(serializers.ModelSerializer):
  class Meta:
    model = Upload
    fields = ['quality']
    
class PrivacySerializer(serializers.ModelSerializer):
  class Meta:
    model = Upload
    fields = ['privacy']
    