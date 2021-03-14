from app import app
from waitress import serve
from paste.translogger import TransLogger

print("Starting...")
serve(TransLogger(app), port=8080)