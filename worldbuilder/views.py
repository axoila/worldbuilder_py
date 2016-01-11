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

def WorldView(request, world_id):
    world = get_object_or_404(World, pk=world_id)
    context = {'world': world}
    return render(request, 'worldbuilder/world.html', context)

def EntryView(request, world_id, entry_id):
    try:
        world = World.objects.get(pk=world_id)
        entry = get_object_or_404(world.entry_set, pk=entry_id)
    except World.DoesNotExist:
        raise Http404("No Entry matches the given query.")
    context = {'entry': entry}
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
