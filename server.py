from app import app
from waitress import serve
from paste.translogger import TransLogger

serve(TransLogger(app), port=8080)