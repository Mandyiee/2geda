from rest_framework import serializers
from .models import Settings

class MyFeedSerializer(serializers.ModelSerializer):
  class Meta:
    model = Settings
    fields = ['myFeeds']
    
class OtherFeedSerializer(serializers.ModelSerializer):
  class Meta:
    model = Settings
    fields = ['otherFeeds']
    
class TaggingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Settings
    fields = ['tagging']