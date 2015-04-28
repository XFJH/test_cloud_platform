from django.conf.urls import patterns, url

from weixin import views

urlpatterns = patterns('',
	# ex: /digs/
	url(r'^$', views.index, name='index'),
	# ex: /digs/5/
    url(r'validate', views.validate, name="validate"),

)