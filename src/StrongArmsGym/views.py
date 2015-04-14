from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib import messages
from django.core.context_processors import csrf
# Create your views here.

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
		return render_to_response('login.html', {}, context)




@login_required
def restricted(request):
	return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
	#log the user out
	logout(request)

	return HttpResponseRedirect('/')