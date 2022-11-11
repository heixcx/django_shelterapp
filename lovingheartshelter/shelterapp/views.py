from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from . import models
from .forms import AdoptForm

# Render home page
def index(request):

	# If user logs in, replace the login/signup link 
	# with user personal page/logout link
	if request.session.get('is_login', None): 
		context = { 
			'loginlink': '/shelterapp/my/',
			'logintext': request.session.get('user_name'),
			'otherlink': '/shelterapp/logout/',
			'othertext': 'Logout'		
		}
		return render(request, 'shelterapp/index.html', context)
	else:
		context = {
			'loginlink': '/shelterapp/login/',
			'logintext': 'Login',
			'otherlink': '/shelterapp/register/',
			'othertext': 'Sign Up'
		}
		return render(request, 'shelterapp/index.html', context)

# Render adopt page
def animals(request):
	if request.session.get('is_login', None):
		context = { 
			'loginlink': '/shelterapp/my/',
			'logintext': request.session.get('user_name'),
			'otherlink': '/shelterapp/logout/',
			'othertext': 'Logout'
		}
		return render(request, 'shelterapp/adopt.html', context)
	else:
		context = { 
			'loginlink': '/shelterapp/login/',
			'logintext': 'Login',
			'otherlink': '/shelterapp/register/',
			'othertext': 'Sign Up'
		}
		return render(request, 'shelterapp/adopt.html', context)

# Render animal detail page
def animal_detail(request, id):
	if request.session.get('is_login', None):
		context = { 
			'loginlink': '/shelterapp/my/',
			'logintext': request.session.get('user_name'),
			'otherlink': '/shelterapp/logout/',
			'othertext': 'Logout'	
		}
		return render(request, 'shelterapp/kitollie.html', context)
	else:
		context = { 
			'loginlink': '/shelterapp/login/',
			'logintext': 'Login',
			'otherlink': '/shelterapp/register/',
			'othertext': 'Sign Up'
		}
		return render(request, 'shelterapp/kitollie.html', context)

# Render login page
def login(request):
	if request.method == "POST":
		loginemail = request.POST.get('email')
		password = request.POST.get('password')
		if loginemail.strip() and password:

			# If couldn't find any existing user who has 
			# the same email address then report error message
			try: 
				user = models.User.objects.get(email=loginemail)
			except :
				message = 'User does not exist!'
				return render(request, 'shelterapp/login.html', {'message': message})

			# If the input password matches, replace the login/signup 
			# link with user personal page/logout link, otherwise report
			# error message
			if user.password == password:
				request.session['is_login'] = True
				request.session['user_id'] = user.id
				request.session['user_name'] = user.firstname
				context = { 
					'loginlink': '/shelterapp/my/',
					'logintext': request.session['user_name'],
					'otherlink': '/shelterapp/logout/',
					'othertext': 'Logout'
				}
				return render(request, 'shelterapp/index.html', context)
			else:
				message = 'Password incorrect!'
				return render(request, 'shelterapp/login.html', {'message': message})
		else:
			return render(request, 'shelterapp/login.html', {'message': message})
	return render(request, 'shelterapp/login.html')

# Render signup page
def register(request):
	context = { 
		'loginlink': '/shelterapp/login/',
		'logintext': 'Login',
		'otherlink': '/shelterapp/register/',
		'othertext': 'Sign Up'
	}
	return render(request, 'shelterapp/signup.html', context)

# User logout and return to login page
def logout(request):
	if not request.session.get('is_login', None):
		return redirect("/shelterapp/login/")
	request.session.flush()
	return redirect("/shelterapp/login/")

# Render user presonal page
def mypage(request):

	# query user's appliations by user id 
	query = models.Application.objects.filter(user_id=request.session.get('user_id'))
	context = { 
		'loginlink': '/shelterapp/my/',
		'logintext': request.session['user_name'],
		'otherlink': '/shelterapp/logout/',
		'othertext': 'Logout',
		'queryresult': query
	}
	return render(request, 'shelterapp/mypage.html', context)

# Store application to database and send updated application data 
# to browser for rendering
def save_application(request, form, template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			user = models.User.objects.get(id=request.session.get('user_id'))
			form.instance.user = user
			form.save()
			data['form_is_valid'] = True
			query = models.Application.objects.filter(user_id=request.session.get('user_id'))
			data['html_application_list'] = render_to_string('shelterapp/application_list.html', {
				'queryresult': query
			})
		else:
			data['form_is_valid'] = False
	context = {'form': form}
	data['html_form'] = render_to_string(template_name, context, request=request)
	return JsonResponse(data)

# Prepare a new form instance and pass it with application create temaplte 
# to save_application function
def create_new(request):
	if request.method == 'POST':
		form = AdoptForm(request.POST)
	else:
		form = AdoptForm()
	return save_application(request, form, 'shelterapp/application_create.html')

# Retrieve the existing form instance by application id 
# and pass it with application info temaplte to save_application function
def view_application(request, id):
	application = get_object_or_404(models.Application, id=id)
	form = AdoptForm(instance=application)
	return save_application(request, form, 'shelterapp/application_info.html')

# Retrieve the existing form instance by application id 
# and pass it with application update temaplte to save_application function
def update_application(request, id):
	application = get_object_or_404(models.Application, id=id)
	if request.method == 'POST':
		form = AdoptForm(request.POST, instance=application)
	else:
		form = AdoptForm(instance=application)
	return save_application(request, form, 'shelterapp/application_update.html')

# def create_new(request):
# 	if request.session.get('is_login', None):
# 		if request.method == 'POST':
# 			adopt_form = forms.AdoptForm(request.POST)
# 			if adopt_form.is_valid():
# 				user = models.User.objects.get(id=request.session.get('user_id'))
# 				adopt_form.instance.user = user
# 				adopt_form.save()
# 				message = 'New adoption application created!'
# 				return render(request, '/shelterapp/my/',{'message': message})
# 			else:
# 				message = 'Creating ew application failed!'
# 				adopt_form = forms.AdoptForm()
# 				return render(request, 'shelterapp/application.html', {'message': message})
# 		context = { 
# 			'loginlink': '/shelterapp/my/',
# 			'logintext': request.session.get('user_name'),
# 			'otherlink': '/shelterapp/logout/',
# 			'othertext': 'Logout',	
# 			'adopt_form': forms.AdoptForm()
# 		}
# 		# adopt_form = forms.AdoptForm()
# 		return render(request, 'shelterapp/application.html', context)
# 	else:
# 		return redirect('/shelterapp/login')
