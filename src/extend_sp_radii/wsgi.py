"""
WSGI config for extend_sp_radii project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

print ('===== sys.path / PYTHONPATH =====')
for k in sorted(os.environ.keys()):
    v = os.environ[k]
        print ('%-30s %s' % (k,v[:70]))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "extend_sp_radii.settings")

application = get_wsgi_application()
