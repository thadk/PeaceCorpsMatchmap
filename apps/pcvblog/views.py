from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from apps.pcvblog.models import Entry
from apps.pcvblog.forms import EntryForm

# The delete class requires a confirm template which we will do in JS
def entry_delete(request, entry_pk):
    entry = get_object_or_404(Entry, pk=entry_pk)
    entry.delete()
    return HttpResponseRedirect(reverse_lazy('entry_list'))


class EntryCreate(CreateView):
    model = Entry
    form_class = EntryForm

    ## TODO: Login required

    def form_valid(self, form):
        ## TODO: Make sure you can only edit your own entry
        form.instance.author_id = self.request.user.pk
        return super(EntryCreate, self).form_valid(form)


class EntryUpdate(UpdateView):
    model = Entry
    form_class = EntryForm


class EntryList(ListView):
    model = Entry
    context_object_name = "entry_list"
    template_name = "templates/entry_list.html"
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Entry.objects.all()
        else:
            return Entry.objects.filter(author__pk=self.request.user.pk)
