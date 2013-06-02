# Create your views here.


class DebugMixin(object):
    """
    For use in testing out a new view
    """
    def get_context_data(self, **kwargs):
        "This is to print your context variables during testing ONLY"
        context = super(DebugMixin, self).get_context_data(**kwargs)
        print "#########################"
        print "CONTEXT SENT TO TEMPLATE:"
        import pdb; pdb.set_trace()
        for k, v in context.items():
            print "  %s: %s" % (k, v)
        print "DON'T FORGET TO REMOVE THIS MIXIN AFTER TESTING THE VIEW"
        print "#########################"        
        return context
