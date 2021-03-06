__author__ = 'snake'

import sys, os

sys.path.append('/home/snake/PycharmProjects/ask_abashin')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ask_abashin.settings'
from models import *
from django.contrib.auth.models import User


def get_page(request):
    page = request.GET.get('qpage')
    if page is None:
        page = 1
    return int(page)


def get_apage(request):
    page = request.GET.get('apage')
    if page is None:
        page = 1
    return int(page)


def get_pages_bounds(pages_count, page):
    if page <= 5:
        page_left = 1
    else:
        page_left = page - 4

    if page < 5 and pages_count >= 10:
        page_right = 10
    elif page < pages_count - 5:
        page_right = page + 5
    else:
        page_right = pages_count
    return page_left, page_right


def get_questions():
    return Question.objects.order_by('-creation_date')[:10]


def get_questions_by_date(page, count=10):
    return Question.objects.order_by('-creation_date')[(page-1)*count:page*count]


def get_latest_users(number=10):
    profs = UserProfile.objects.order_by('-rating')[:number]
    usrs = []
    for x in profs:
        usr = get_users_by_id(x.user_id)
        usrs.append(usr)

    return User.objects.order_by('-date_joined')[:number], usrs


def get_answers_by_date(page, count=10):
    return Answer.objects.order_by('-date')[(page-1)*count:page*count]


def get_answers_by_question(qid):
    return Answer.objects.filter(question=get_questions_by_id(qid)).order_by('-date').order_by('-rating')


def get_questions_by_user(page, uid, count=10):
    return Question.objects.filter(author=get_users_by_id(uid)).order_by('-date').order_by('-rating')[(page-1)*count:page*count]


def get_all_questions_by_user(uid):
    return Question.objects.filter(author=get_users_by_id(uid))


def get_answers_by_user(page, uid, count=10):
    return Answer.objects.filter(author=get_users_by_id(uid)).order_by('-date').order_by('-rating')[(page-1)*count:page*count]


def get_all_answers_by_user(uid):
    return Answer.objects.filter(author=get_users_by_id(uid))


def get_questions_by_id(qid):
    return Question.objects.get(pk=qid)


def get_answers_by_id(aid):
    return Answer.objects.get(pk=aid)


def get_users_by_id(uid):
    return User.objects.get(pk=uid)


def get_questions_by_rating(page, count=10):
    return Question.objects.order_by('-rating')[(page-1)*count:page*count]


def get_answers_by_rating(page, count=10):
    return Answer.objects.order_by('-rating')[(page-1)*count:page*count]


def get_votes_by_user_and_question(uid, qid, vtp):
    try:
        res = VoteQuestion.objects.get(user=get_users_by_id(uid), question=get_questions_by_id(qid), vote_type=vtp)
    except VoteQuestion.DoesNotExist:
        res = None
    return res


def RemoveQVote(uid, qid, vtp):
    try:
        VoteQuestion.objects.get(user=get_users_by_id(uid), question=get_questions_by_id(qid), vote_type=vtp).delete()
    except VoteQuestion.DoesNotExist:
        return 1
    return 0


def get_votes_by_user_and_answer(uid, aid, vtp):
    try:
        res = VoteAnswer.objects.get(user=get_users_by_id(uid), answer=get_answers_by_id(aid), vote_type=vtp)
    except VoteAnswer.DoesNotExist:
        res = None
    return res


def RemoveAVote(uid, aid, vtp):
    try:
        VoteAnswer.objects.get(user=get_users_by_id(uid), answer=get_answers_by_id(aid), vote_type=vtp).delete()
    except VoteAnswer.DoesNotExist:
        return 1
    return 0


def get_user_by_username(uname):
    try:
        res = User.objects.get(username=uname)
    except User.DoesNotExist:
        return None
    return res.id
