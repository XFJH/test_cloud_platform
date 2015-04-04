from django.contrib import admin

# Register your models here.
from django.contrib import admin
from digs.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['question_text']}),
		('Date information',{'fields': ['pub_date'], 'classes':['collapse']}),
	]
	list_display =('question_text', 'pub_date','was_published_recently')
	list_filter = ['pub_date']
	
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)