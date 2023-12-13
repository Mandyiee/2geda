from django.db import models
from userprofile.models import Profile
# Create your models here.

class Stereo(models.Model):
  DOWNLOADCHOICES = (
    ('any','Any'),
    ('wifi','WI-FI Only Download'),
    ('mobile','Mobile Data')
  )
  QUALITYCHOICES = (
    ('auto','Auto'),
    ('high','High'),
    ('low','Low')
  )
  profile = models.OneToOneField(Profile,models.CASCADE,related_name='stereo')
  quality = models.CharField(choices=QUALITYCHOICES,max_length=30,blank=True,null=True,default='auto')
  offlineDownload = models.CharField(choices=DOWNLOADCHOICES,max_length=30,blank=True,null=True,default='any')
  
  def __str__(self):
    return self.profile