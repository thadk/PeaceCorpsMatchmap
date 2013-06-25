from django.views.generic import TemplateView, ListView, View

from apps.pcvblog.models import Entry
from .map_utils import Ajaxify, get_map_data

import utils
print utils.__dict__.keys()

from utils.views import JSONListView

class MapView(TemplateView):

    template_name = "map/main.html"

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context["data"] = get_map_data()
        return context


class DataOptionsJSON(Ajaxify, View):
    def dispatch(self, request, *args, **kwargs):
        json_dict = {
            "data": get_map_data()
        }
        return self.render_json_response(json_dict)


# class BlogJSON(Ajaxify, ListView):
#     """
#     This should also pass country locations and counts.

#     pagination is available, but not tested yet
#     filter format:
#     /map/get_blogs?country=Uganda&sector=Environment
#     get_queryset can hold the filter logic, check out the commented
#     out (untested) example.
#     """
#     # paginate_by = 5
#     model = Entry

#     def get_queryset(self):
#         entries = super(BlogJSON, self).get_queryset()
#         filters = self.request.REQUEST
#         print filters
#         if "country" in filters:
#             entries = entries.filter(
#                 author__pcvprofile__country=filters["country"]
#             )
#         if "sector" in filters:
#             entries = entries.filter(
#                 author__pcvprofile__sector=filters["sector"]
#             )
#         if "gradelevel" in filters:
#             entries = entries.filter(
#                 grade_level=filters["gradelevel"]
#             )
#         if "homestate" in filters:
#             entries = entries.filter(
#                 author__pcvprofile__home_state=filters["homestate"]
#             )
#         return entries

#     def dispatch(self, request, *args, **kwargs):
#         # get pagination from the default get() method
#         json_dict = {
#             "posts": self.serialize_blog_entries(),
#             # add country= {"name":"UG", "lat":32424, "long":08545}
#         }
#         return self.render_json_response(json_dict)



class BlogJSON(JSONListView):
    model = Entry
    paginate_by = 5

    def get_queryset(self):
        entries = super(BlogJSON, self).get_queryset()
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