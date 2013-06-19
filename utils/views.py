from django import http
from django.views.generic.list import BaseListView

from .serialize import json_encode


class JSONResponseMixin(object):
    """
    View mixin that renders a JSON response (the context serialized).

    See ``ezbake.utils.serialize.json_encode`` for details on how the
    context is serialized.

    This mixin can also allow views to return JSON only in certain cases, using
    just the ``get_json_response`` method where needed.
    """
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(context)

    def get_json_response(self, context, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(json_encode(context),
                                 content_type='application/json',
                                 **httpresponse_kwargs)


class JSONListView(BaseListView, JSONResponseMixin):
    """
    View that responds with a JSON-serialized list of model instances.

    Pagination and other features found in ``django.views.generic.ListView``
    are also optionally provided.

    Example::

        class BookListView(JSONListView):
            model = Book
            paginate_by = 5 # five objects per page

            def get_queryset(self):
                qs = self.model.objects.filter(author=self.kwargs['author'])
                return qs

        GET /author/5/books/?page=2
        --> {
            "meta": {
                "is_paginated": true,
                "total_count": 15
                "page": 2,
            },
            "objects": [
                {
                    "title": "The Fox and The Goat",
                    "description": "A sad little 'tail'.",
                    ...
                },
                ... (4 more)
            ]
        }
    """
    def get_context_data(self, **kwargs):
        data = super(JSONListView, self).get_context_data(**kwargs)
        objects = data['object_list']
        is_paginated = data['is_paginated']
        page = data['page_obj']
        paginator = data['paginator']
        return {
            'meta': {
                # TODO add pagination info here using data['paginator'], ...
                'page': page.number if is_paginated else None,
                'total_count': paginator.count if is_paginated else len(objects),
                'is_paginated': is_paginated
            },
            'objects': objects
        }
