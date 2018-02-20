# Custom decorator for views see Django by Example pg 161
# A decorator is a function that takes another function and extends the behavior of the latter without explicitly modifying it.
# Further reading https://www.python.org/dev/peps/pep-0318/
# To be used for ajax views
# It defines a wrap function that returns an HttpResponseBadRequest object (HTTP 400 code) if the request is not AJAX. 
# Otherwise, it returns the decorated function.

from django.http import HttpResponseBadRequest


def ajax_required(f):
    def wrap(request, *args, **kwargs):
            if not request.is_ajax():
                return HttpResponseBadRequest()
            return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap