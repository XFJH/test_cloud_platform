from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dig_author.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'weixin/', include('weixin.urls', namespace='weixin')),
    # url(r'^', include('digs.urls', namespace='digs')), # dig entrance
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# customizing error views

handler500 = 'digs.views.page_error'

# Sending email
send_mail('Subject here', 'Here is the message.', '1258080923@qq.com',
    ['941078420@qq.com'], fail_silently=False)

handler500 = 'digs.views.page_error'

