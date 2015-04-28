from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
from django.core.mail import send_mail
=======
>>>>>>> 1c819ed0293209c8bca3b460e2fabd5998c49b02

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dig_author.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
<<<<<<< HEAD

    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'weixin/', include('weixin.urls', namespace='weixin')),
=======
    
>>>>>>> 1c819ed0293209c8bca3b460e2fabd5998c49b02
    url(r'^', include('digs.urls', namespace='digs')),
    url(r'^admin/', include(admin.site.urls)),
)

# customizing error views
<<<<<<< HEAD
handler500 = 'digs.views.page_error'

# Sending email
send_mail('Subject here', 'Here is the message.', '1258080923@qq.com',
    ['941078420@qq.com'], fail_silently=False)
=======
handler500 = 'digs.views.page_error'
>>>>>>> 1c819ed0293209c8bca3b460e2fabd5998c49b02
