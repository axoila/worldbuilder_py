from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from worldbuilder_py.forms import MyRegistrationForm
# from django.contrib.formtools.wizard.views import SessionWizardView
# from django.core.mail import send_mail
#
# from celery.result import AsyncResult
# from celery_test.tasks import do_something_long
from django.core.urlresolvers import reverse
# from django.utils import simplejson as json

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('loggedin'))
    else:
        return HttpResponseRedirect(reverse('invalid'))

def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    else:
        form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')
