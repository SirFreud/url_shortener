from django.conf import settings;
from django_hosts import patterns, host
from main.hostsconf import urls

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'main.hostsconf.urls', name='wildcard'),
)