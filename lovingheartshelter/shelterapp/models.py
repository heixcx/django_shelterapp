from django.db import models

# User data model
class User(models.Model):

	firstname = models.CharField(max_length=128, unique=True)
	lastname = models.CharField(max_length=128, unique=True)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=256)
	mobile = models.CharField(max_length=32)
	c_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s %s" % (self.firstname, self.lastname)

# Adoption application data model
class Application(models.Model):

	user = models.ForeignKey(User,on_delete=models.CASCADE) # User id as a foreign key in application model
	driverlicense = models.CharField(max_length=128)
	address = models.CharField(max_length=256)
	animalname = models.CharField(max_length=128)
	animalid = models.CharField(max_length=128)
	otherpets = models.CharField(max_length=256)
	homecheck = models.CharField(max_length=128)
	checkcalls = models.CharField(max_length=128)
	c_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s %s" % (self.user.firstname, self.c_time)

  