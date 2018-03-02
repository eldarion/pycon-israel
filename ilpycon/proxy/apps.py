from __future__ import unicode_literals
from django.apps import AppConfig


class ProxyConfig(AppConfig):
    name = "ilpycon.proxy"
    label = "proxy"
    verbose_name = _("Proxy")
