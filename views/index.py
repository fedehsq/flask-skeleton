import os
from flask import render_template, blueprints
from flask import current_app

# Create a blueprint
index = blueprints.Blueprint('index', __name__)

# Define the index route
@index.route('/')
def home():
    # Get all files in the static directory
    videos = os.listdir('static/videos')
    host = current_app.config['HOST']
    videos = [host + '/static/videos/' + video for video in videos]
    return render_template('index.html', videos=videos)