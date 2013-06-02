from django.views.generic import TemplateView, ListView, View

from braces.views import JSONResponseMixin

import data_options, sample_json

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


class BlogJSON(JSONResponseMixin, View):

    def get(self, request, *args, **kwargs):
        context = {
            'posts': sample_json.posts
        }
        return self.render_json_response(context)
