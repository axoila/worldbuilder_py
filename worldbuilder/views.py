from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import World, Entry, Variable


class IndexView(generic.ListView):
    template_name = 'worldbuilder/index.html'
    context_object_name = 'worlds'

    def get_queryset(self):
        """Return all worlds"""
        return World.objects.all()


class WorldView(generic.DetailView):
    model = World
    template_name = 'worldbuilder/detail.html'


class EntryView(generic.DetailView):
    model = Entry
    template_name = 'worldbuilder/results.html'

# def modifyEntry(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'worldbuilder/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('worldbuilder:results', args=(question.id,)))
