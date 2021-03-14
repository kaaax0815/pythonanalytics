from flask import *
import fortnitepy.analytics
import os

app = Flask(__name__)
app.add_url_rule('/fortnitepy/analytics', view_func=fortnitepy.analytics.analytics, methods=['POST'])

@app.route('/')
def index():
    return render_template('index.html')