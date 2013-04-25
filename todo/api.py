#!/usr/bin/env python
# coding: UTF-8

from tastypie import fields, http
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

from models import Task

import datetime

class DjangoAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        if getattr(request, 'user', False) and request.user.is_authenticated():
            return True
        return False 

    def get_identifier(self, request):
        return request.user.username

class TaskResource(ModelResource):
    class Meta:
        include_resource_uri = True
        queryset = Task.objects.all()
        resource_name = 'task'
        filtering = {'title': ALL}
        authorization = Authorization()
        authentication = DjangoAuthentication()
        
        
    def get_object_list(self, request):
        query = super(TaskResource, self).get_object_list(request)
        query = query.filter(user=request.user)
        return query 