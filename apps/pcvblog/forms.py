from django import forms

from apps.pcvblog.models import Entry


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('title', 'body')
