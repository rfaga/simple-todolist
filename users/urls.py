#!/usr/bin/env python

from django.conf.urls.defaults import patterns, url

from django.conf import settings

#import django.contrib.auth.views

urlpatterns = patterns('users.views',
    url(r'^login/$', 'login', name='users_login'),
    url(r'^logout/$', 'logout', name='users_logout'), 
    url(r'^new/$', 'new', name='users_new_user'),
)

