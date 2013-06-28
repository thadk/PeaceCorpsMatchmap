from django.views.generic import ListView, DetailView

from utils.views import JSONListView
from apps.worldmap.map_utils import get_map_data, make_geojson

from .models import Entry
from .forms import EntryForm

class BlogFilterMixin(object):
    """
    Filters the queryset by country, sector, gradelevel, and homestate,
    as passed through in request parameters
    """
    model = Entry

    def get_queryset(self):
        entries = super(BlogFilterMixin, self).get_queryset()
        filters = self.request.REQUEST
        if "country" in filters:
            entries = entries.filter(
                author__pcvprofile__country=filters["country"]
            )
        if "sector" in filters:
            entries = entries.filter(
                author__pcvprofile__sector=filters["sector"]
            )
        if "gradelevel" in filters:
            entries = entries.filter(
                grade_level=filters["gradelevel"]
            )
        if "homestate" in filters:
            entries = entries.filter(
                author__pcvprofile__home_state=filters["homestate"]
            )
        return entries


class BlogJSON(BlogFilterMixin, JSONListView):
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(BlogJSON, self).get_context_data(**kwargs)
        context['countries'] = make_geojson([entry.author.pcvprofile.country for entry in self.object_list])
        return context

class Entries(BlogFilterMixin, ListView):
    template_name = "blog/entry_list.html"
    paginate_by = 10

    def get_queryset(self, **kwargs):
        entries = super(Entries, self).get_queryset()
        # import pdb
        # pdb.set_trace()
        self.pcv = self.kwargs.get("pcv", "")
        if self.pcv:
            entries = entries.filter(author__username=self.pcv)
        return entries

class Permalink(DetailView):
    template_name = "blog/permalink.html"
    model = Entry