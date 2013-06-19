import datetime

from decimal import Decimal

from django.db.models import Model, ImageField, FileField
from django.db.models.query import QuerySet
from django.utils.functional import Promise
from django.utils.encoding import force_unicode
from django.utils import simplejson as json
from django.utils.simplejson import JSONEncoder
from django.utils import datetime_safe

class ExtendedJSONEncoder(JSONEncoder):
    """
    Extesion of the ``JSONEncoder`` to be used as an encoder class for
    ``simplejson.dumps``.  The ``DjangoJSONEncoder`` gives us correct
    serialization of date/time and Decimal types.  This extension goes further
    to handle Django model objects, giving an alternative to Django's
    serialization module.  Unlike the standard django serialization fromework,
    this can handle dynamically-added attributes.  In addition, it checks for
    ``as_dict`` and ``as_list`` attributes (can be method, property, etc.) on
    objects, which are used to encode first if they exist.

    Some of this is based off of dojango json_encode function.
    (see http://code.google.com/p/dojango/)

    TODO IMPORTANT determine copywrite on dojango code
    """
    # TODO way to custom-specify date format... and also use date format from settings as default
    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"

    def default(self, o):
        def _call_or_access(x):
            """Call if callable, otherwise just access."""
            return x() if hasattr(x, '__call__') else x

        if hasattr(o, 'as_dict'):
            # TODO as_dict circular reference checking fail
            d = _call_or_access(o.as_dict)
            if isinstance(d, dict):
                return d
            else:
                raise TypeError("as_dict method did not return a dict")
        elif hasattr(o, 'as_list'):
            # TODO as_list circular reference checking fail
            l = _call_or_access(o.as_list)
            if isinstance(l, list):
                return l
            else:
                raise TypeError("as_list method did not return a list")
        elif isinstance(o, QuerySet):
            # treat as list
            return list(o)
        elif isinstance(o, Model):
            return self._model_as_dict(o)
        elif isinstance(o, Promise):
            # see http://code.djangoproject.com/ticket/5868
            return force_unicode(o)
        elif isinstance(o, Decimal):
            # json.dumps() cant handle Decimal
            return str(o)
        elif isinstance(o, datetime.datetime):
            d = datetime_safe.new_datetime(o)
            return d.strftime("%s %s" % (self.DATE_FORMAT, self.TIME_FORMAT))
        elif isinstance(o, datetime.date):
            d = datetime_safe.new_date(o)
            return d.strftime(self.DATE_FORMAT)
        elif isinstance(o, datetime.time):
            return o.strftime(self.TIME_FORMAT)
        else:
            return super(ExtendedJSONEncoder, self).default(o)

    def _begin_circular_ref_checking(self, model_obj):
        """Marks that we have seen this Django model object in our current
        nesting-level context; used for circular-reference checking."""
        if not hasattr(self, '_model_markers'):
            self._model_markers = {}
        markerid = id(model_obj)
        if markerid in self._model_markers:
            raise ValueError("Circular reference detected")
        self._model_markers[markerid] = model_obj

    def _end_circular_ref_checking(self, model_obj):
        """Removes Django model object marker (for circular-reference
        checking).  This is called at the end of the same level of nesting as
        _add_model_marker was, indicating that we are free of any circular-
        references for the object.
        """
        markerid = id(model_obj)
        if hasattr(self, '_model_markers') and markerid in self._model_markers:
            del self._model_markers[markerid]

    def _model_as_dict(self, o):
        """Converts a model to a dict which can then be encoded."""
        ret = {}

        if self.check_circular:
            self._begin_circular_ref_checking(o)

        # Add any standard model fields
        for f in o._meta.fields:
            f_obj = getattr(o, f.attname)

            # special FileField handling (they can't be json serialized)
            if isinstance(f, ImageField) or isinstance(f, FileField):
                ret[f.attname] = unicode(f_obj)
            else:
                ret[f.attname] = f_obj

        # And additionally encode arbitrary properties that had been added.
        fields = dir(o.__class__) + ret.keys()
        add_ons = [k for k in dir(o) if k not in fields
                                     # ignore _state and delete properties
                                     and k not in ('delete', '_state',)
                                     # ignore marked-as-private attributes
                                     and len(k) > 0 and k[0] != '_']
        for a in add_ons:
            a_obj = getattr(o, a)
            ret[a] = a_obj

        if self.check_circular:
            self._end_circular_ref_checking(o)

        return ret


class HumanizedDateEncoder(json.JSONEncoder):
    """
    HumanizedDateEncoder class for representing date values as string
    """
    def default(self, obj):
        # For date values returns representing string:
        if isinstance(obj, datetime.date):
            value = datetime.date(obj.year, obj.month, obj.day)
            delta = value - datetime.date.today()
            if delta.days == 0:
                return (u'today')
            elif delta.days == 1:
                return (u'tomorrow')
            elif delta.days == -1:
                return (u'yesterday')
            else:
                return (u'%s days ago' % abs(delta.days))
        else:
            return json.JSONEncoder.default(self, obj)


def json_encode(obj):
    """Serializes the object as json using simplejson.dumps, with the
    ``ExtendedJSONEncoder`` as the encoder class.  A different
    encoder can be specified with the kwarg."""
    return ExtendedJSONEncoder().encode(obj)
