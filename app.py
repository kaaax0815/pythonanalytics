from gevent import monkey
monkey.patch_all()

import os
from gevent.pywsgi import WSGIServer
from api import app

http_server = WSGIServer(('0.0.0.0', 8080), app)
print("Starting Server...")
try:
    http_server.serve_forever()
except KeyboardInterrupt:
    print("Exiting...")