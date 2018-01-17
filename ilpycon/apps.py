from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "ilpycon"

    def ready(self):
        import_module("ilpycon.receivers")
