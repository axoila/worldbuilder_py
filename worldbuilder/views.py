from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django.views import generic
# from django.utils import timezone
# from django import forms
from worldbuilder.forms import EntryForm
from django.template.context_processors import csrf
from django.contrib.auth.models import User

from .models import World, Entry, Variable


def IndexView(request):
    userList = User.objects.all()
    context = {'users': userList}
    return render(request, 'worldbuilder/index.html', context)

def userView(request, user_name):
    user = User.objects.get(username=user_name)
    worlds = user.world_set.all()
    context = {'worlds': worlds, 'user': user}
    return render(request, 'worldbuilder/user.html', context)

def WorldView(request, user_name, world_name):
    user = User.objects.get(username=user_name)
    world = user.world_set.get(name=world_name)
    entries = world.entry_set.all()
    context = {'entries':entries, 'world': world, 'user': user}
    return render(request, 'worldbuilder/world.html', context)

def EntryView(request, user_name, world_name, entry_name):
    user = User.objects.get(username=user_name)
    world = user.world_set.get(name=world_name)
    entry = world.entry_set.get(name=entry_name)
    variables = entry.variable_set.all()
    context = {'variables':variables, 'entry':entry, 'world': world, 'user': user}
    return render(request, 'worldbuilder/entry.html', context)

def createEntry(request):
    if(request.POST):
        form = EntryForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('worldbuilder:index'))
    else:
        form = EntryForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('worldbuilder/create_entry.html', args)
