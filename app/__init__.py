from flask import Flask, request, abort, jsonify, Blueprint, render_template

application = Flask(__name__)
app = application

from . import api
app.register_blueprint(api.bp)

from . import site
app.register_blueprint(site.bp)

from . import stats
app.jinja_env.globals['apis'] = stats.apis
app.jinja_env.globals['accounts'] = stats.accounts

@app.after_request
def after_request(response):
    csp = "default-src 'self' 'unsafe-inline' https://*.googleapis.com https://*.google.com https://*.gstatic.com https://cdnjs.cloudflare.com https://use.fontawesome.com"
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['Content-Security-Policy'] = csp
    return response
    
if __name__ == "__main__":         
    app.run()