from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import ShortenedURL


# This is a function-based view
def shortened_redirect_view(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(ShortenedURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)


# This is a class based view
class ShortenedCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortenedURL, shortcode=shortcode)
        return HttpResponse("hello again {sc}".format(sc=shortcode))

    def post(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse()

# print(request.user)
# print(request.user.is_authenticated())
# print(shortcode)
    # try:
    #     obj = ShortenedURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = ShortenedURL.objects.all().first()
    # Either the above or below methods would work if we wanted something OTHER than a 404 error to display when we hit a wrong page
    # obj_url = None
    # qs = ShortenedURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url
