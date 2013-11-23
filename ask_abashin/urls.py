from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ask import views
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^index$', views.index, name='index'),
                       url(r'^ask$', views.ask, name='ask'),
                       url(r'^answer$', views.answer, name='answer'),
                       url(r'^qpopular', views.questions_by_rating),
                       url(r'^apopular$', views.answers_by_rating),
                       url(r'^ans_correct$', views.ans_correct),
                       url(r'^answers', views.answers),
                       url(r'^users', views.users),


)
