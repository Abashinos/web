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


class VoteQuestion(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey('Question')
    value = models.IntegerField(max_length=4)


class VoteAnswer(models.Model):
    user = models.ForeignKey(User)
    answer = models.ForeignKey('Answer')
    value = models.IntegerField(max_length=4)


class CommentQuestion(models.Model):
    contents = models.CharField(max_length=500)
    date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class CommentAnswer(models.Model):
    contents = models.CharField(max_length=500)
    date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

