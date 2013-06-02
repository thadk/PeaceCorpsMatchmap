from django import forms
from django.core.exceptions import ValidationError

from braces.forms import UserKwargModelFormMixin

from apps.pcvblog.models import Entry


class EntryForm(UserKwargModelFormMixin, forms.ModelForm):
    def clean(self, *args, **kwargs):
        #self.image = kwargs.pop('image', None)
        if self.instance.pk:
            if not self.instance.author == self.user:
                raise ValidationError('You can only edit your own post')
        # if not self.user.pcvprofile.pk:
        #     raise ValidationError('Only PCVs can create posts')
        return super(EntryForm, self).clean(*args, **kwargs)

    class Meta:
        model = Entry
        fields = ('title', 'body', 'image')
