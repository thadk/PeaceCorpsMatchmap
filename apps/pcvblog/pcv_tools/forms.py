from django import forms
from django.core.exceptions import ValidationError

from braces.forms import UserKwargModelFormMixin
from taggit.models import Tag

from apps.pcvblog.models import Entry

def choices_from_tags(tag_qs):
    return [(tag.name, tag.name) for tag in tag_qs]

class EntryForm(UserKwargModelFormMixin, forms.ModelForm):
    tags = forms.MultipleChoiceField(
        required=False,
        choices=choices_from_tags(Tag.objects.all())
    )

    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        if self.instance.pk is not None:
            tag_names = self.instance.tags.all().values_list('name', flat=True)
            self.fields['tags'].initial = tag_names

    def clean(self, *args, **kwargs):
        if self.instance.pk:
            if not self.instance.author == self.user:
                raise ValidationError('You can only edit your own post')
        # if not self.user.pcvprofile.pk:
        #     raise ValidationError('Only PCVs can create posts')
        return super(EntryForm, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        entry = super(EntryForm, self).save(*args, **kwargs)
        entry.tags.set(*self.cleaned_data['tags'])
        return entry

    class Meta:
        model = Entry
        fields = ('title', 'body', 'image', 'grade_level')
