from django.db import models

# Create your models here.
class User:
    id = models.AutoField(primary_key=True)
    name = models.CharField('name',max_length=50)
    gender = models.CharField('gender')
    nick_name = models.CharField('nick name',max_length=30)
    avatar = models.CharField('avatar')
    facebookID = models.CharField('facebook id')
    timestamp = models.DateField('create time',auto_now=True)
    reputation = models.FloatField('score')
    description = models.CharField('description',max_length = 500)
    email = models.CharField('email',max_length=50)
    phone = models.CharField('phone')
    #created_tasks = models.ManyToManyField(Task)
    #accepted_tasks = models.ManyToManyField(Task)
    
class Task:
    id = models.AutoField(primary_key=True)
    name = models.CharField('name',max_length=50)
    type = models.CharField('Type',max_length=30)
    description = models.CharField('description',max_length = 500)
    number_needed = models.IntegerField('number of perople needed')
    timestamp = models.DateField('create time',auto_now=True)
    need_time = models.DateField('need time')
    lat = models.FloatField('lat')
    lon = models.FloatField('lon')
    #creator = models.ForeignKey('User')
    #challenger = models.ManyToManyField('User')
    
class Honor:
    id = models.AutoField(primary_key=True)
    name = models.CharField('name',max_length=50)
    description = models.CharField('description',max_length = 500)
    
    
    