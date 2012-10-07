from django.http import HttpResponseRedirect

def direct(request):
	return HttpResponseRedirect("/account/login/")