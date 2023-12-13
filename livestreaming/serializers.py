from rest_framework import serializers
from .models import Livestreaming

class AudioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Livestreaming
    fields = ['audioQuality']
    
class VideoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Livestreaming
    fields = ['videoQuality']
    
