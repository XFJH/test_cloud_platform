from django.conf.urls import patterns, url

from digs import views

urlpatterns = patterns('',
	# ex: /digs/
	url(r'^$', views.index, name='index'),
	# ex: /digs/5/
	url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
	# ex: /digs/5/results/
	url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
	# ex: /digs/5/vote/
	url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    
    url(r'^all/$', views.all_author, name='all'),
)