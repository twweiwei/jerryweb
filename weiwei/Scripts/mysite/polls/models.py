# trips/models.py
import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
# Create your models here.

@python_2_unicode_compatible 
class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

@python_2_unicode_compatible 
class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    



@python_2_unicode_compatible 
class Post(models.Model):
    # ...
    def __str__(self):
        return self.學號

    學號 = models.CharField(max_length=100)
    姓名 = models.CharField(max_length=100)
    
    # trips/admin.py
