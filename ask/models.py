from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.forms import ModelForm


class Question(models.Model):
    header = models.CharField(max_length=500)
    contents = models.CharField(max_length=1500)
    author = models.ForeignKey(User)
    creation_date = models.DateTimeField()
    rating = models.IntegerField()


class Answer(models.Model):
    contents = models.CharField(max_length=1500)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
    date = models.DateTimeField()
    correct = models.BooleanField()
    rating = models.IntegerField()


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['header', 'contents']


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['contents']

