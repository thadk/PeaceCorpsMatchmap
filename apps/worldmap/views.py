from django.views.generic import TemplateView, ListView, View

from apps.pcvblog.models import Entry

from .utils import Ajaxify
import data_options

class MapView(TemplateView):

    template_name = "map/main.html"

    def get_map_data(self):
        data = {
            "countries": data_options.COUNTRIES,
            "states":    data_options.STATES,
            "sectors":   data_options.SECTORS,
            "keywords":  data_options.KEYWORDS,
            "grades":    data_options.GRADES
        }
        return data


    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context["data"] = self.get_map_data()
        return context


class BlogJSON(Ajaxify, ListView):
    """
    pagination is available, but not tested yet
    filter format:
    /map/get_blogs?country=Uganda&sector=Environment
    get_queryset can hold the filter logic, check out the commented
    out (untested) example.
    """
    # paginate_by = 5
    model = Entry

    def get_queryset(self):
        entries = super(BlogJSON, self).get_queryset()
        filters = self.request.REQUEST
        print filters
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

    def dispatch(self, request, *args, **kwargs):
        json_dict = {
            "posts": self.serialize_blog_entries(),
        }
        return self.render_json_response(json_dict)
