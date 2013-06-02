from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from braces.views import LoginRequiredMixin, UserFormKwargsMixin


from apps.pcvblog.models import Entry
from apps.pcvblog.forms import EntryForm

class BlogLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')

class ImageUploadMixin(object):
    def get_form_kwargs(self):
        import pdb; pdb.set_trace()
        kwargs = super(ImageUploadMixin, self).get_form_kwargs()
        if self.request.FILES:
            kwargs['files'] = self.request.FILES
        return kwargs


# The delete class requires a confirm template which we will do in JS
def entry_delete(request, entry_pk):
    entry = get_object_or_404(Entry, pk=entry_pk)
    if not entry.author == request.user:
        return HttpResponse('Unauthorized', status=401)
    else:
        entry.delete()
        return HttpResponseRedirect(reverse_lazy('entry_list'))


class EntryCreate(ImageUploadMixin, BlogLoginRequiredMixin, UserFormKwargsMixin, CreateView):
    model = Entry
    form_class = EntryForm

    def form_valid(self, form):
        ## TODO: Make sure you can only edit your own entry
        form.instance.author_id = self.request.user.pk
        return super(EntryCreate, self).form_valid(form)


class EntryUpdate(ImageUploadMixin, BlogLoginRequiredMixin, UserFormKwargsMixin, UpdateView):
    model = Entry
    form_class = EntryForm


class EntryList(ListView, UserFormKwargsMixin):
    model = Entry
    context_object_name = "entry_list"
    template_name = "templates/entry_list.html"
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Entry.objects.all()
        else:
            return Entry.objects.filter(author__pk=self.request.user.pk)
