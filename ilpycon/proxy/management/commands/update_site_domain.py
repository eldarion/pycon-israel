from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Updates the current site's domain based on
        `settings.FORCE_SCRIPT_NAME`
        """
        site = Site.objects.get_current()
        site_domain = site.domain
        self.stdout.write(f"Current site domain: {site_domain}")

        proxy_path = getattr(settings, "FORCE_SCRIPT_NAME") or ""

        domain_part = site_domain.split("/").pop(0)
        desired_site_domain = f"{domain_part}{proxy_path}"
        self.stdout.write(f"Desired site domain: {desired_site_domain}")
        if site_domain != desired_site_domain:
            site.domain = desired_site_domain
            site.save()
            self.stdout.write(f"Updated site domain to: {site.domain}")
        else:
            self.stdout.write(f"No site domain change was required")
