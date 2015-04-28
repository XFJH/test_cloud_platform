from django.db import models

# Create your models here.
class Author(models.Model):
    nickname = models.CharField(max_length=200)
    yyid = models.CharField(max_length=200, unique=True)
    uid = models.CharField(max_length=200)
    yyNo = models.CharField(max_length=30)

class Video(models.Model):
    rawId = models.CharField(max_length=200, unique=True)
    snampshotUrl = models.CharField(max_length=200)
    wordCut = models.CharField(max_length=200)
    playTimes = models.CharField(max_length=200)
    durations = models.CharField(max_length=200)
    feedId = models.CharField(max_length=30)
    author = models.ForeignKey(Author) 
    create_date = models.DateField('date created')