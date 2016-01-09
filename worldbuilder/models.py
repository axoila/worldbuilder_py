import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class World(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def entry_count(self):
        if self.entry_set is None:
            return "-"
        else:
            return self.entry_set.count()

@python_2_unicode_compatible
class Entry(models.Model):
    world = models.ForeignKey(World, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def variable_count(self):
        if self.variable_set is None:
            return "-"
        else:
            return self.variable_set.count()

@python_2_unicode_compatible
class Variable(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="-")
    value = models.CharField(max_length=200, default="-")
    def __str__(self):
        return self.name
