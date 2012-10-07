from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from activation import activate_user
from django.http import HttpResponseRedirect, Http404
 
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = RegisterForm()
 
    return render_to_response("accounts/register.html",  {'form': form,  },context_instance=RequestContext(request))
	
		
def activate(request):
    user = request.GET.get('user')
    code = request.GET.get('code')
 
    if activate_user(user,  code):
        return HttpResponseRedirect("/")
    else:
        raise Http404