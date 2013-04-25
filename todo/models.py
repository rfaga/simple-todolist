#!/usr/bin/env python
# coding: UTF-8

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
# Create your models here.

from django.contrib.auth.models import User
from django.utils import datetime_safe
#from set.tools.choices import *
#from set.tools import audit

import datetime



PRIORITIES = (
    ('1', u'Very High'),
    ('2', u'High'),
    ('3', u'Normal'),
    ('4', u'Low'),
    ('5', u'Very Low'),
)

class Task(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField('Description', blank=True)
    date = models.DateTimeField(null=True, blank=True)
    place = models.CharField(max_length=128, blank=True )
    priority = models.CharField(choices=PRIORITIES, max_length=1, default='3')
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['priority',]
    

