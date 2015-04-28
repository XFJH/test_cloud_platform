# -*- encoding: utf-8 -*- #
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader, TemplateDoesNotExist
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django import forms

import hashlib
import json

# Create your views here.
def index(request):
    return HttpResponse('hello world')

def validate(request):
    if request.method == "GET":
        token = "weixin_validate_string"
        signature = request.GET['signature']
        timestamp  = request.GET['timestamp']
        nonce = request.GET['nonce']
        echostr = request.GET['echostr']
        tmpstr = ''.join(sorted([token, timestamp, nonce]))
        hashstr = hashlib.sha1(tmpstr).hexdigest()

        if hashstr == signature:
            return_str = echostr
        else:
            return_str = 'validate fail' + json.dumps(request.GET)
        return HttpResponse( return_str )
    elif request.method == 'POST':
        return HttpResponse('hello world')
    else:
        return HttpResponse('else')

def page_error(request):
	return HttpResponse("500")