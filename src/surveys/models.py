from __future__ import unicode_literals

from django.db import models

from companies.models import Company
from users.models import Customer

class Survey(models.Model):
	company = models.ForeignKey(Company)
	name = models.CharField(max_length=25)

	def __unicode__(self): #def __str__(self):
		return self.name

	# get question set


STYLE_CHOICES = (
	('rate', 'Rating'),
	('text', 'Text Response'),
)

class Question(models.Model)
	survey	 = models.ForeignKey(Survey)
	question = models.TextField(max_length=500)
	style = models.CharField(max_length=25, choices=STYLE_CHOICES)

class Answer(models.Model):
	question = models.ForeignKey(Question)
	response_text = models.TextField(max_length=500)
	response_rate = models.PositiveIntegerField(min_value=1, max_value=10)

class SurveyResponse(models.Model):
	customer = models.ForeignKey(Customer)
	survey = models.ForeignKey(Survey)
	answer = models.ManyToMany(Answer)

	completed = models.BooleanField()

	customer_age = models.DateField()
	start_time = models.DateField(auto_now_add=True)
	last_edited = models.DateField(auto_now=True)
	
	# location = 

	# is complete (create function to see if each question has an answer)




