__author__ = 'snake'
import sys,os
sys.path.append('/home/snake/PycharmProjects/ask_abashin/ask_abashin')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.conf import settings
from ask.models import Question
from django.contrib.auth.models import User

# selection of all questions of certain user
print Question.objects.count()
