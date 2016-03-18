from __future__ import unicode_literals

from django.db import models

class user(models.Model):
	user_id	= models.IntegerField() 
	name    = models.CharField(max_length=100, blank=True, default='')  
	email   = models.CharField(max_length=100, blank=True, default='') 
	destination =  models.CharField(max_length=100, blank=True, default='')
	price =  models.IntegerField()
	class Meta:
		ordering = ('user_id',)
 
class book_ticket(models.Model):
	user_id    = models.IntegerField() 
	ticket_id  = models.IntegerField() 
 
class ticket(models.Model):
	ticket_id 		= models.IntegerField() 
	seat_id  		= models.IntegerField() 
	aircomp 		= models.CharField(max_length=100, blank=True, default='') 
	flight_number 	= models.IntegerField()
	price 			= models.IntegerField()
	destination 	= models.CharField(max_length=100, blank=True, default='')  
	booked 		= models.BooleanField()

	class Meta:
		ordering = ('ticket_id',)
 

