
from braces.views import JSONResponseMixin, AjaxResponseMixin


class Ajaxify(JSONResponseMixin, AjaxResponseMixin):
    """
    Stores serialization methods and AJAXy braces
    """

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