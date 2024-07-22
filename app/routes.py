import logging
from flask import send_from_directory, render_template

logging.basicConfig(level=logging.DEBUG)

def serve_static_js(filename):
    logging.debug(f"Serving static js: {filename}")
    return send_from_directory('templates/static/js', filename)

def serve_static_css(filename):
    logging.debug(f"Serving static css: {filename}")
    return send_from_directory('templates/static/css', filename)

def serve_react_app(path=None):
    logging.debug(f"Serving path: {path}")
    return render_template('index.html')

