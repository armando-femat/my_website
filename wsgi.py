import sys
import os
import os.path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                'mysite')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
