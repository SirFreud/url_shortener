from django.conf.urls import url
from django.contrib import admin
# Instead of importing the entire views file, only import the functions or classes that you need
from shortener.views import HomeView, ShortenedCBView
# DO NOT DO
# from shortener import views
# from another_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    # Example of a slug url regular expression
    # url(r'^a/(?P<shortcode>[\w-]+){6, 20}/$', shortened_redirect_view),
    url(r'^b/(?P<shortcode>[\w-]+){6, 20}/$', ShortenedCBView.as_view()),
    # DO NOT DO
    # url(r'abc', shortener.views.shortened_redirect_view),
    # url(r'abc', views.shortened_redirect_view),
]


