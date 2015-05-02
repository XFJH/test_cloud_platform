# -*- encoding: utf-8 -*- #
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader, TemplateDoesNotExist
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django import forms
from lxml import etree
import time

import hashlib
import json

# Create your views here.
def index(request):
    return HttpResponse('hello world')

@csrf_exempt
def validate(request):
    try:
        token = "weixin_validate_string"
        signature = request.GET['signature']
        timestamp  = request.GET['timestamp']
        nonce = request.GET['nonce']
        tmpstr = ''.join(sorted([token, timestamp, nonce]))
        hashstr = hashlib.sha1(tmpstr).hexdigest()
        if hashstr == signature:
            if request.method == "GET":
                token = "weixin_validate_string"
                signature = request.GET['signature']
                timestamp  = request.GET['timestamp']
                nonce = request.GET['nonce']
                tmpstr = ''.join(sorted([token, timestamp, nonce]))
                hashstr = hashlib.sha1(tmpstr).hexdigest()
                if hashstr == signature:
                    echostr = request.GET['echostr']
                    return_str = echostr
                else:
                    return_str = 'validate fail' + json.dumps(request.GET)
                return HttpResponse( return_str )
            elif request.method == 'POST':
                body = request.body.decode('utf8')
                dic_body = {}
                parser = etree.XMLParser(strip_cdata=False)
                root = etree.XML(body, parser)
                for item in list(root):
                    dic_body[item.tag] = item.text
                # begin realy do something base MsgType: text, image, voice, video, music
                if dic_body['MsgType'] == 'text':
                    res = etree.Element('xml')
                    ToUserName = etree.SubElement(res, "ToUserName")
                    FromUserName = etree.SubElement(res, "FromUserName")
                    CreateTime = etree.SubElement(res, "CreateTime")
                    MsgType = etree.SubElement(res, "MsgType")
                    Content = etree.SubElement(res, "Content")
                    ToUserName.text = etree.CDATA(dic_body['FromUserName'])
                    FromUserName.text = etree.CDATA(dic_body['ToUserName'])
                    CreateTime.text = str(time.time())
                    MsgType.text = etree.CDATA('text')
                    # below content.text is thing to be motify
                    Content.text = etree.CDATA('welcome to wo~zhubo')
                    return HttpResponse(etree.tostring(res))
                else:
                    pass
            else:
                return HttpResponse('else')
    except:
        return HttpResponse('hello')

def page_error(request):
	return HttpResponse("500")