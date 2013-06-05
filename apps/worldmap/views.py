from django.views.generic import TemplateView, ListView, View

from braces.views import JSONResponseMixin, AjaxResponseMixin

from apps.pcvblog.models import Entry
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


class BlogJSON(JSONResponseMixin, AjaxResponseMixin, ListView):
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
        # if "country" in filters:
        #     # something like this...
        #     entries = entries.filter('author__pcvprofile'=filters['country'])
        return entries

    def serialize_pcv(self, user):
        return {
            "username": user.username,
            "name": "%s %s" % (user.first_name, user.last_name),
            # "sector": user.pcvprofile.sector,
            # "country": user.pcvprofile.country,
        }

    def serialize_blog_entries(self):
        queryset = self.get_queryset()
        entries = []
        for entry in queryset:
            json_entry = {
                "title": entry.title,
                "text": entry.body,
                "slug": entry.slug,
                "date": entry.post_time,
                "user": self.serialize_pcv(entry.author),
            }
            entries.append(json_entry)
        return entries

    def dispatch(self, request, *args, **kwargs):
        json_dict = {
            "posts": self.serialize_blog_entries(),
        }
        return self.render_json_response(json_dict)
