from django.views.generic import TemplateView
import data_options

class MapView(TemplateView):
    template_name = "map/main.html"

    def get_map_data(self):
        data = {
            "countries": data_options.COUNTRIES,
            "states": data_options.STATES,
        }
        return data


    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context["data"] = self.get_map_data()
        return context