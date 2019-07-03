from flask import Flask, request, abort, jsonify, Blueprint, render_template

def create_app(test_config=None):

    app = Flask(__name__)

    from . import api
    app.register_blueprint(api.bp)

    from . import site
    app.register_blueprint(site.bp)

    from . import stats
    app.jinja_env.globals['apis'] = stats.apis()
    app.jinja_env.globals['accounts'] = stats.accounts()
    app.jinja_env.globals['sitekey'] = stats.sitekey()

    @app.after_request
    def after_request(response):
        csp = "default-src 'self' 'unsafe-inline' https://*.googleapis.com https://*.google.com https://*.gstatic.com https://cdnjs.cloudflare.com https://use.fontawesome.com"
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Content-Security-Policy'] = csp
        return response
    
    return app