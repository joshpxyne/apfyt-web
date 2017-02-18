from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Company(models.Model):
	name = models.CharField(max_length=25)
	bio = models.TextField(max_length=500, blank=True)
	
	def __unicode__(self): #def __str__(self):
		return self.name

class CompanyApfytManager(models.Model):
	company = models.ForeignKey(Company)
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	
class Customer(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	birth_year = models.DateField()

