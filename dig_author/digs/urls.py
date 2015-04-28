from django.conf.urls import patterns, url

from digs import views

urlpatterns = patterns('',
	# ex: /digs/
	url(r'^$', views.index, name='index'),
)