from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls), name='admin'),
)

urlpatterns += patterns('pbook.views',
    url(r'^$', 'index', name='home'),
    url(r'^book/(?P<book_id>\d+)/$', 'view_book', name='book'),
    url(r'^contact/(?P<contact_id>\d+)/$', 'view_contact', name='contact'),
)

urlpatterns += staticfiles_urlpatterns()
