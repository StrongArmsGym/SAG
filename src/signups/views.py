from django.contrib.auth import authenticate, login
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib import messages
from django.core.context_processors import csrf
# Create your views here.
from .forms import UserForm, UserProfileForm

def home(request):

	return render_to_response("main-landing.html", 
							locals(),
							context_instance=RequestContext(request))

def register(request):
	# get the request's context.
	context = RequestContext(request)

	#a boolean value: whether registration was successful or not
	registered = False #initial set to false


	if request.method == 'POST':

		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			#save the user's form data to the database.
			user = user_form.save()

			#hash password.
			user.set_password(user.password)
			#update user object.
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			# did the user provide  a pic?	
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']


			# save the UserProfile model instance.
			profile.save()

			#update var, tell template registration was successful
			registered = True

			username = request.POST['username']
			password = request.POST['password']

			u = authenticate(username=username, password=password)
			if u:
				if u.is_active:
					login(request, u)
					return HttpResponseRedirect('@' + username)
					#return render(request, 'profile.html', {'profile': profile})

		else:
			print user_form.errors, profile_form.errors
    #Not a HTTP POST, so we render our form using two ModelForm instances
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	#Render the template depending on the context.
	return render_to_response(
			'register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
			context
		)

def user_login(request):
	# Obtain the context for the user's request.
	context = RequestContext(request)

	# If the request is a HTTP POST, try to pull info
	if request.method == "POST":
		# Gather the username and password provided.
		username = request.POST['username']
		password = request.POST['password']

		# Check Validity of U / P
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect("Your SAG account is disabled.")
		else:
			#incorrect login
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponseRedirect("Invalid login details supplied.")
	#The request is not a HTTP POST, display login form
	else:
		# blank dictionary object bc no context variables to pass to the template
		return render_to_response('/login.html', {}, context)




def thankyou(request):

	return render_to_response("thankyou.html", 
							locals(),
							context_instance=RequestContext(request))

def aboutus(request):

	return render_to_response("aboutus.html", 
							locals(),
							context_instance=RequestContext(request))


