from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import *
from ask.models import *

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['header', 'contents']


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['contents']


class CommentQuestionForm(ModelForm):
    class Meta:
        model = CommentQuestion
        fields = ['contents']

class CommentAnswerForm(ModelForm):
    class Meta:
        model = CommentAnswer
        fields = ['contents']


class RegistrationForm (UserCreationForm):

    first_name = CharField(max_length=30,
                                  label="First name",
                                  required=False)

    last_name = CharField(max_length=30,
                                 label="Last name",
                                 required=False)

    email = EmailField(label="E-mail")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
