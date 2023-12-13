from django.db import models
from userprofile.models import Profile
# Create your models here.

class Upload(models.Model):
  QUALITYCHOICES = (
    ('auto','Auto'),
    ('original','Original Quality'),
     ('high','High'),
    ('low','Low')
  )
  PRIVACYCHOICES = (
    ('private','Private'),
    ('public','Public'),
    ('friends','Friends Only')
  )
  profile = models.OneToOneField(Profile,models.CASCADE,related_name='Upload')
  quality = models.CharField(choices=QUALITYCHOICES,max_length=30,blank=True,null=True,default='auto')
  privacy = models.CharField(choices=PRIVACYCHOICES,max_length=30,blank=True,null=True,default='private')
  
  def __str__(self):
    return self.profile