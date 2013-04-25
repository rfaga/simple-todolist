#!/usr/bin/env python
# coding: UTF-8

from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _, check_for_language

from django.contrib.auth import views

from django.views.decorators.cache import never_cache
import urlparse
#from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm,\
    AuthenticationForm



def login(request, next=None):
    ans = views.login(request, template_name='users/login.html', authentication_form=AuthenticationForm, extra_context={'next': next})
    if next and request.user.is_authenticated():
        return redirect(reverse('todo_index'))
    else:
        return ans

def logout(request):
    return views.logout(request, next_page='/')
                                                          
@never_cache
def new(request, usp=None):
    data = {}

    if request.POST:        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = request.POST['password1']
            request.POST = QueryDict('username=%s&password=%s'% (user.username, password) )
            return login(request, next)
    else:
        form = UserCreationForm()
    data['form'] = form
    return render_to_response('users/create.html', data, context_instance=RequestContext(request))
