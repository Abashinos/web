__author__ = 'snake'
import sys,os
sys.path.append('/home/snake/PycharmProjects/ask_abashin/ask_abashin')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.conf import settings
from ask.models import Question, Answer
from django.contrib.auth.models import User


# sample change of header
Question.objects.filter(pk=45569).update(header="Zis question")

# expire old answers
#Answer.objects.filter(pk__lt__=100, correct=0).update(contents="expired answer")

# strip all superusers of privileges
#User.objects.filter(superuser=1).update(superuser=0)