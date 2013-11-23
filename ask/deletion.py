__author__ = 'snake'
import sys,os
sys.path.append('/home/snake/PycharmProjects/ask_abashin/ask_abashin')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.conf import settings
from ask.models import Question, Answer
from django.contrib.auth.models import User

# delete all non-staff users
usr = User.objects.filter(is_staff=0)
for x in usr.all():
    x.delete()

# delete all short (length<10) questions
qstn = Question.objects.filter(header__len__lt__=10)
for x in qstn.all():
    x.delete()

# delete all unmarked questions
answr = Answer.objects.filter(correct=0)
for x in answr.all():
    answr.delete()
