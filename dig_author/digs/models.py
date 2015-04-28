from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Author(models.Model):
    nickname = models.CharField(max_length=200)
    # yid means yy's id, ex: 10996888
    yid = models.CharField(max_length=200,)
    # yy user id, ex: e8be86c4f5448e26acc5b4754808fcc8
    uid = models.CharField(max_length=200, )
    # yy Noumber, ex: 118819
    yyNo = models.CharField(max_length=30,)
    # from: search-box, yyzone, ..
    yyNo_from = models.CharField(max_length=30)
    
    def __str__(self):
        return '|'.join((self.nickname, self.yid, self.uid, self.yyNo))

class Video(models.Model):
    rawId = models.CharField(max_length=200)
    snampshotUrl = models.CharField(max_length=200)
    wordCut = models.CharField(max_length=200)
    playTimes = models.CharField(max_length=200)
    durations = models.CharField(max_length=200)
    feedId = models.CharField(max_length=30)
    author = models.ForeignKey(Author)