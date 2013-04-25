from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    
    url(r'^users/', include('users.urls')),
    url(r'^', include('todo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


from tastypie.api import Api

from todo.api import TaskResource 

v1_api = Api(api_name='api')
v1_api.register(TaskResource())
urlpatterns += patterns('',
    (r'', include(v1_api.urls)),
)
