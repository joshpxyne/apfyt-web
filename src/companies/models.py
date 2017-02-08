from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=25)
	bio = models.TextField(max_length=500, blank=True)
	
	def __unicode__(self): #def __str__(self):
		return self.name