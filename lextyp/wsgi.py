"""
WSGI config for lextyp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
import site
from django.core.wsgi import get_wsgi_application

site.addsitedir('/home/akondratjeva/env/lib/python3.5/site-packages')

sys.path.append('/home/akondratjeva/nonsemiotic')
sys.path.append('/home/akondratjeva/nonsemiotic/lextyp')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lextyp.settings")

activate_env=os.path.expanduser('/home/akondratjeva/env/bin/activate_this.py')
#execfile(activate_env, dict(__file__=activate_env))
exec(compile(open(activate_env, "rb").read(), activate_env, 'exec'), dict(__file__=activate_env))

application = get_wsgi_application()
