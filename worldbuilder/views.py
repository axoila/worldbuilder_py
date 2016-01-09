from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import World, Entry, Variable


def IndexView(request):
    worldList = World.objects.all()
    context = {'worlds': worldList}
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

def modifyEntry(request, question_id): #NOT WORKING!!
    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'worldbuilder/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
        return HttpResponseRedirect(reverse('worldbuilder:results', args=(question.id,)))
