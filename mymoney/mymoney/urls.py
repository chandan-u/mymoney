from django.conf.urls import patterns, include, url

from django.contrib.auth.views import login, logout
from django.contrib.auth import REDIRECT_FIELD_NAME

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mymoney.views.home', name='home'),
    # url(r'^mymoney/', include('mymoney.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    #account login/logout views
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^$', 'mymoney.apps.User.views.home', name='homepage'),
    url(r'^user/home$', 'mymoney.apps.User.views.home', name='user_home')
)
