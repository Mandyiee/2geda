from django.db import models
from userprofile.models import Profile
# Create your models here.

class Livestreaming(models.Model):
  VIDEOCHOICES = (
    ('auto','Auto'),
    ('higher','Higher Picture Quality'),
    ('saver','Data Saver')
  )
  AUDIOCHOICES = (
    ('auto','Auto'),
    ('high','High'),
    ('low','Low')
  )
  profile = models.OneToOneField(Profile,models.CASCADE,related_name='livestreaming')
  videoQuality = models.CharField(choices=VIDEOCHOICES,max_length=30,blank=True,null=True,default='auto')
  audioQuality = models.CharField(choices=AUDIOCHOICES,max_length=30,blank=True,null=True,default='auto')
  
  def __str__(self):
    return self.profile