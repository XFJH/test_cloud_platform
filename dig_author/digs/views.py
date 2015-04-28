# -*- encoding: utf-8 -*- #
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from digs.models import Question, Choice, Author
from django.template import RequestContext, loader, TemplateDoesNotExist
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django import forms

# Create your views here.
def index(request):
	if request.method == 'POST':
		#try:
		anchor_yyNo = request.POST['anchor_yyNo']
		if anchor_yyNo.isdigit() and len(anchor_yyNo) < 20:
			try:
				anchor = Author.objects.get(yyNo=anchor_yyNo)
				#anchor = get_object_or_404(Author, yyNo=anchor_yyNo)
			except ObjectDoesNotExist:
				auchor = Author(yyNo=anchor_yyNo, yyNo_from="search-box")
				auchor.save()

			# dream responseble
			# 根据YY号给出YY号所属主播的视频列表
			context = { 'pid_template': "format_dig_data/"+anchor_yyNo+".html",
		                #'anchor': anchor,
		              }
			try:
				return render(request, 'digs/b_index.htm', context)
			except TemplateDoesNotExist:
				context = {'get_error': True}
				return render(request, 'digs/index.html', context)
			#return HttpResponse(anchor.yyNo_from)
		else:
			return HttpResponse( 'No anchor found')
	else:
		context = {'author_list': 'digs/yyNo_list.html' }
		return render(request, 'digs/index.html', context)


def page_error(request):
	return HttpResponse("500")