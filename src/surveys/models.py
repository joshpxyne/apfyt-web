from __future__ import unicode_literals
from django.db import models
from users.models import Customer, Company 
from django.core.validators import MinValueValidator, MaxValueValidator

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

class Question(models.Model):
	survey	 = models.ForeignKey(Survey)
	question = models.TextField(max_length=500)
	style = models.CharField(max_length=25, choices=STYLE_CHOICES)

	order = models.PositiveIntegerField(default=0)

	def __unicode__(self): #def __str__(self):
		return str(self.survey) + ", question " + str(self.order) 

	class Meta:
		unique_together = ('survey', 'question')
        ordering = ('order',)

STATUS_CHOICES = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
)

class Answer(models.Model):
	question = models.ForeignKey(Question)
	response_text = models.TextField(max_length=500, null=True, blank=True)
	response_rate = models.PositiveIntegerField(
		choices=STATUS_CHOICES, 
		validators=[MinValueValidator(1), MaxValueValidator(10)], 
		null=True, 
		blank=True)

	def __unicode__(self): #def __str__(self):
		return "Answer: " + str(self.question) 

class SurveyResponse(models.Model):
	customer = models.ForeignKey(Customer)
	survey = models.ForeignKey(Survey)
	answer = models.ManyToManyField(Answer)

	completed = models.BooleanField()

	customer_age = models.DateField()
	start_time = models.DateField(auto_now_add=True)
	last_edited = models.DateField(auto_now=True)
	
	def __unicode__(self): #def __str__(self):
		return "Response: " + str(self.survey)
	# location = 

	# is complete (create function to see if each question has an answer)




