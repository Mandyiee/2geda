from django.db import models
from userprofile.models import Profile
# Create your models here.

class Tv(models.Model):
  QUALITYCHOICES = (
    ('auto','Auto'),
    ('higher','Higher Picture Quality'),
    ('saver','Data Saver')
  )
  DOWNLOADCHOICES = (
    ('any','Any'),
    ('wifi','WI-FI Only Download'),
    ('mobile','Mobile Data')
  )
  profile = models.OneToOneField(Profile,models.CASCADE,related_name='tv')
  quality = models.CharField(choices=QUALITYCHOICES,max_length=30,blank=True,null=True,default='auto')
  offlineDownload = models.CharField(choices=DOWNLOADCHOICES,max_length=30,blank=True,null=True,default='any')
  
  def __str__(self):
    return self.profile