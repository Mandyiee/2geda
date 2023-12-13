from django.db import models
from userprofile.models import Profile
# Create your models here.

class Settings(models.Model):
  PRIVACYCHOICES = (
    ('public','Public'),
    ('private','Private')
  )
  profile = models.OneToOneField(Profile,models.CASCADE,related_name='setting')
  myFeeds = models.CharField(choices=PRIVACYCHOICES,max_length=10,blank=True,null=True,default='public')
  otherFeeds = models.CharField(choices=PRIVACYCHOICES,max_length=10,blank=True,null=True,default='public')
  tagging = models.CharField(choices=PRIVACYCHOICES,max_length=10,blank=True,null=True,default='public')
  
  def __str__(self):
    return self.profile