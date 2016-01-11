from django import forms
from worldbuilder.models import Entry, World

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('name', 'world', )
