from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dig_author.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^', include('digs.urls', namespace='digs')),
    url(r'^admin/', include(admin.site.urls)),
)

# customizing error views
handler500 = 'digs.views.page_error'