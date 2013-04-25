#!/usr/bin/env python

from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('todo.views',
    url(r'^$', 'index',  name='todo_index'),
    url(r'^list/$', 'ajax_list',  name='todo_list'),
    url(r'^edit/(?P<task>.*)$', 'edit',  name='todo_edit'),
    url(r'^new/$', 'edit',  name='todo_new'),
    url(r'^remove/(?P<task>.*)$', 'remove',  name='todo_remove'),
)
