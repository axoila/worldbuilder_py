import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class World(models.Model):
    world_name = models.CharField(max_length=200)
    def __str__(self):
        return self.world_name
    def entry_count(self):
        return len(World.objects.all())

@python_2_unicode_compatible
class Entry(models.Model):
    world = models.ForeignKey(World, on_delete=models.CASCADE)
    entry_name = models.CharField(max_length=200)
    def __str__(self):
        return self.entry_name

class Variable(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

class TextEntry(Variable):
    value = ""
