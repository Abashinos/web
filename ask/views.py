# Create your views here.
import datetime
from math import ceil
import random
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.template import loader, Context, RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from ask.forms import *
from scripts import *
from django.contrib.auth.views import login as djlogin
from django.contrib.auth.views import logout as djlogout


def index(request):

    usrs = get_latest_users()

    qpage = get_page(request)
    qstns = get_questions_by_date(qpage)

    pagecount = int(ceil(Question.objects.count()/10 + 1))
    page_left, page_right = get_pages_bounds(pagecount, qpage)

    allpages = range(page_left, page_right + 1)

    c = {
        "questions": qstns,
        "uusers": usrs,
        "pages_count": pagecount,
        "page": "",
        "current_page": qpage,
        "pages": allpages}

    return render(request, "index.html", c)

def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    if not request.method == 'POST':
        regform = RegistrationForm()
    else:
        regform = RegistrationForm(request.POST)
        if regform.is_valid():
            _user = regform.save()
            _user = authenticate(username=request.POST['username'], password=request.POST['password2'])
            login(request, _user)
            try:
                redir = request.GET['next']
            except:
                raise Http404
            return HttpResponseRedirect(redir)

        else:
            usrs = get_latest_users()
            return render(request, "registration.html", {
                                    'regform': regform,
                                    'uusers': usrs
                                    })

    usrs = get_latest_users()
    return render(request, "registration.html", {
        'regform': regform,
        'uusers': usrs
    })


def log_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    usrs = get_latest_users()
    c = { 'uusers': usrs }

    return djlogin(request, extra_context=c)


def log_out(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')

    return djlogout(request)


def comment_question(request):
    err = {"error": "The comment is invalid."}
    if request.method == 'POST':
        form = CommentQuestionForm(request.POST)
        if form.is_valid():
            usr = request.user
            conts = form.cleaned_data['contents']
            qid = int(form.data['q_id'])
            try:
                qstn = Question.objects.get(id=qid)
            except qstn.DoesNotExist:
                return render(request, 'errors.html', err)
            comt = CommentQuestion.objects.create(contents=conts, question_id=qid, author=usr, date=datetime.datetime.now())
            comt.save()
            redir = request.META['HTTP_REFERER']
            return HttpResponseRedirect(redir)
        else:
            return render(request, 'errors.html', err)
    else:
        return render(request, 'errors.html', err)


def ask(request):
    err = {"error": "Your question has invalid parameters. Check length of header and contents."}
    if request.method == 'POST':
        qform = QuestionForm(request.POST)

        if qform.is_valid():
            usr = request.user
            hdr = qform.cleaned_data['header']
            cnts = qform.cleaned_data['contents']
            qstn = Question.objects.create(header=hdr, contents=cnts, author= usr, rating=0, creation_date=datetime.datetime.now())
            qstn.save()
            return HttpResponseRedirect("/index")
        else:
            return render(request, "errors.html", err)
    else:
        return render(request, "errors.html", err)


def questions_by_rating(request):
    usrs = get_latest_users()
    qpage = get_page(request)
    qstns = get_questions_by_rating(qpage)

    pagecount = int(ceil(Question.objects.count()/10 + 1))
    page_left, page_right = get_pages_bounds(pagecount, qpage)

    allpages = range(page_left, page_right + 1)

    c = {
        "questions": qstns,
        "uusers": usrs,
        "pages_count": pagecount,
        "page": "qpopular",
        "current_page": qpage,
        "pages": allpages}

    return render(request, "index.html", c)


def answer(request):
    err = {"error": "The answer is invalid. Check its length"}
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            usr = request.user
            conts = form.cleaned_data['contents']
            qid = int(form.data['qid'])
            answr = Answer.objects.create(contents=conts, author=usr, question_id=qid, rating=0, date=datetime.datetime.now())
            answr.save()
            redir = request.META['HTTP_REFERER']
            return HttpResponseRedirect(redir)
        else:
            return render(request, 'registration/../templates/errors.html', err)
    else:
        return render(request, 'registration/../templates/errors.html', err)


def answers(request):

    usrs = get_latest_users()

    if request.GET.get('qnum') is None:

        apage = get_apage(request)
        answs = get_answers_by_date(apage)

        pagecount = int(ceil(Answer.objects.count()/10 + 1))
        page_left, page_right = get_pages_bounds(pagecount, apage)

        allpages = range(page_left, page_right + 1)

        c = {
        "answers": answs,
        "uusers": usrs,
        "pages_count": pagecount,
        "page": "answers",
        "current_page": apage,
        "pages": allpages}

        return render(request, "index.html", c)

    else:

        qstn_id = int(request.GET['qnum'])
        qstn = get_questions_by_id(qstn_id)
        answs = get_answers_by_question(qstn_id)

        t = loader.get_template("answers.html")
        c = RequestContext(request, {"question": qstn,
                     "uusers": usrs,
                     "answers": answs})

        return HttpResponse(t.render(c))


def answers_by_rating(request):

    usrs = get_latest_users()
    apage = get_apage(request)
    answs = get_answers_by_rating(apage)

    pagecount = int(ceil(Answer.objects.count()/10 + 1))
    page_left, page_right = get_pages_bounds(pagecount, apage)

    allpages = range(page_left, page_right + 1)

    c = {
        "answers": answs,
        "uusers": usrs,
        "pages_count": pagecount,
        "page": "apopular",
        "current_page": apage,
        "pages": allpages}

    return render(request, "index.html", c)


def users(request):

    usrs = get_latest_users()

    if request.GET.get("tab") == "questions" or request.GET.get("tab") is None:
        try:
            usr = get_users_by_id(int(request.GET['num']))
            qpage = get_page(request)
            qstns = get_questions_by_user(qpage, usr.id)

            temp_qstns = get_all_questions_by_user(usr.id)
            pagecount = int(ceil(temp_qstns.count()/10 + 1))
            page_left, page_right = get_pages_bounds(pagecount, qpage)

            allpages = range(page_left, page_right + 1)

            c = {"uuser": usr,
                "uusers": usrs,
                "questions": qstns,
                "pages_count": pagecount,
                "page": "questions",
                "current_page": qpage,
                "pages": allpages}

            return render(request, "users.html", c)
        except:
            raise Http404

    elif request.GET.get("tab") == "answers":
        try:
            usr = get_users_by_id(int(request.GET['num']))
            apage = get_apage(request)
            answs = get_answers_by_user(apage, usr.id)

            temp_answs = get_all_answers_by_user(usr.id)
            pagecount = int(ceil(temp_answs.count()/10+1))
            page_left, page_right = get_pages_bounds(pagecount, apage)

            allpages = range(page_left, page_right + 1)

            c = {"uuser": usr,
                "uusers": usrs,
                "answers": answs,
                "pages_count": pagecount,
                "page": "answers",
                "current_page": apage,
                "pages": allpages}

            return render(request, "users.html", c)
        except:
            raise Http404

    else:
        raise Http404


def ans_correct(request):

    err = {"error": "Answer not found"}

    if 'a_id' in request.GET and request.GET['a_id']:
        aid = int(request.GET.get('a_id'))
    else:
        return render(request, 'errors/errors.html', err)
    try:
        Answr = get_answers_by_id(aid)
    except:
        return render(request, 'errors/errors.html', err)

    if Answr.correct:
        Answr.correct = False
    else:
        Answr.correct = True
    Answr.save()

    redir = request.META['HTTP_REFERER']
    return HttpResponseRedirect(redir)