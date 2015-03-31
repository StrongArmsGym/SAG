from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
from django.core.context_processors import csrf
# Create your views here.
from .forms import SignUpForm

def home(request):

	return render_to_response("main-landing.html", 
							locals(),
							context_instance=RequestContext(request))

def signup(request):

	form = SignUpForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'Thank you for joining')
		return HttpResponseRedirect('/thank-you/')
		

	return render_to_response("signup.html", 
							locals(),
							context_instance=RequestContext(request))

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def invalid(request):
	return render_to_response('invalid.html')

def account_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user:
		auth.login(request, user)
		return HttpResponseRedirect('/loggedin')
	else:
		return HttpResponseRedirect('/invalid')

def loggedin(request):
	return render_to_response('loggedin.html',
							{'full_name': request.user.username})
def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')


def thankyou(request):

	return render_to_response("thankyou.html", 
							locals(),
							context_instance=RequestContext(request))

def aboutus(request):

	return render_to_response("aboutus.html", 
							locals(),
							context_instance=RequestContext(request))


