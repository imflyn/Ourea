import sae
from ourea import wsgi

application = sae.create_wsgi_app(wsgi.application)
