#!/usr/bin/env python
# coding: UTF-8

from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.template import RequestContext


from django.contrib.auth.decorators import login_required
from django.core.servers.basehttp import FileWrapper

from datetime import datetime

from models import Task
from forms import TaskForm
from django.views.decorators.csrf import csrf_exempt
### view functions

def index(request):
    tasks = None
    if request.user and request.user.is_authenticated():
        tasks = Task.objects.filter(user=request.user) 
    return render_to_response('home.html', {'tasks': tasks}, context_instance=RequestContext(request))

@login_required
@csrf_exempt
def ajax_list(request):
    tasks = Task.objects.filter(user=request.user) 
    return render_to_response('list.html', 
            {'tasks': tasks}, context_instance=RequestContext(request))


@login_required
@csrf_exempt
def edit(request, task=None):
    args = {}
    if task:
        args['instance'] = get_object_or_404(Task, pk=task)
    else:
        args['user'] = request.user
    print task
    if request.POST:
        form = TaskForm(request.POST, **args)
        if form.is_valid():
            form.save()
            return HttpResponse('')
    else:
        form = TaskForm(**args)
    return render_to_response('edit.html', 
        {'form': form}, context_instance=RequestContext(request))
    

@login_required
@csrf_exempt
def remove(request, task):
    task = get_object_or_404(Task, pk=task)
    task.delete()
    return HttpResponse('')
