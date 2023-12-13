from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Profile(models.Model):
  RELIGONCHOICES = (
    ('christain','Christain'),
    ('islam','Islam'),
    ('traditional','Traditional')
  )
  GENDERCHOICES = (
    ('male','Male'),
    ('female','Female'),
    ('other','Other')
  )
  user = models.ForeignKey(User,models.CASCADE,related_name='profile')
  username = models.CharField(max_length=100,blank=True,null=True)
  firstname =  models.CharField(max_length=100,blank=True,null=True)
  lastname =  models.CharField(max_length=100,blank=True,null=True)
  currentCity =  models.CharField(max_length=100,blank=True,null=True)
  dateOfBirth = models.DateField(blank=True,null=True)
  religon = models.CharField(choices=RELIGONCHOICES,max_length=20,blank=True,null=True)
  gender = models.CharField(choices=GENDERCHOICES,max_length=20,blank=True,null=True)
  customGender = models.CharField(max_length=100,blank=True,null=True)
  backupDetail = models.CharField(max_length=100,blank=True,null=True)
  
  def __str__(self):
    return f'{self.username}'
  
  
  
  
  
  
  
  
  