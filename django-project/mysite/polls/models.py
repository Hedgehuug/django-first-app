import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    # I don't know what to do with these models yet, I'm just making them
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    #No clue what ForeignKey or models.CASCADE does, or on_delete
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    # We used charfield before I'm guessing that's just places to put text
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

