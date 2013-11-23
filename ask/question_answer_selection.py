__author__ = 'snake'
import sys,os
sys.path.append('/home/snake/PycharmProjects/ask_abashin/ask_abashin')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.conf import settings
from ask.models import Question, Answer

# selection of all answers on certain question
qstn = Question.objects.get(pk=10)
answr = Answer.objects.filter(question=qstn)

for x in answr.all():
    print "Answer ID =", x.id, ":\n" + x.contents + "\t"
    if x.correct == 1:
        print "The answer is marked as correct\n"
    else:
        print "The answer has not yet been verified\n"