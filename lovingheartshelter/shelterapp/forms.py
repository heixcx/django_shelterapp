from django.forms import ModelForm
from . import models
from .models import Application

# Form for creating an adopt application
class AdoptForm(ModelForm):
	class Meta:
		model = models.Application
		fields = ['driverlicense', 'address', 'animalname', 'animalid', 'otherpets', 'homecheck', 'checkcalls']
		labels = {
			'driverlicense': "Driver's License / ID*", 
			'address': 'Home Address*', 
			'animalname': 'Animal Nma of Interest*', 
			'animalid': 'Animal ID of Interest*', 
			'otherpets': 'Do you have other pets in your home?*', 
			'homecheck': 'Do you agree to a home-check?*', 
			'checkcalls': 'Do you agree to check-up calls?*'
		}
		exlusive = ['user'] # No need to manunally input user id
	


