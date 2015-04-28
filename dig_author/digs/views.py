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
<<<<<<< HEAD
=======
		#try:
>>>>>>> 1c819ed0293209c8bca3b460e2fabd5998c49b02
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
	
def detail(request, question_id):
	# try:
		# question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
		# raise Http404("Question does not exist")
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'digs/detail.html', {'question': question})
	
def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return HttpResponse(response % question_id)
	
def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'digs/detail.html', {
			'question': p,
			'error_message': "You didn't select a choice",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a 
		# user hits the Back button
		return HttpResponseRedirect(reverse('digs:results', args=(p.id)))
	
def all_author(request):
	author = Author.objects.all()[:5]
	return HttpResponse(author)


def page_error(request):
	return HttpResponse("500")