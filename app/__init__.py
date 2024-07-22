from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates')

    # Import and register routes
    from .routes import serve_static_js, serve_static_css, serve_react_app
    app.add_url_rule('/static/js/<path:filename>', 'serve_js_file', serve_static_js)
    app.add_url_rule('/static/css/<path:filename>', 'serve_css_file', serve_static_css)
    app.add_url_rule('/', 'serve_index', serve_react_app)
    app.add_url_rule('/<path:path>', 'serve_default', serve_react_app)

    return app

