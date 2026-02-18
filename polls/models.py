from django.db import models
import datetime
from django.utils import timezone

# model = the single, definitive source of information about your data
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_created_recently(self):
        dif = self.pub_date - timezone.now()
        return dif <= datetime.timedelta(days=1)

class Choice(models.Model):
    # foreignkey = one question is related to one choice
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


