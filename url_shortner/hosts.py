from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'', settings.ROOT_URLCONF, name='http'),
   # host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
)