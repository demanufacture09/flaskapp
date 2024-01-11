import time
import flask
from flask import Flask

print('Python Modules Imported, Starting up...')

time.sleep(1)
print('In a few moments, webview should initiate...')
time.sleep(1)

def VariablestoBoot():
    htmlfile = '/home/runner/ImportantIntentDebugger/FlaskTemplate/index.html'
    print('HTML File Found')
    cssfile = '/home/runner/ImportantIntentDebugger/FlaskTemplate/style.css'
    print('CSS File Found')
    jsfile = '/home/runner/ImportantIntentDebugger/FlaskTemplate/script.js'
    print('JS File Found')
    return htmlfile, cssfile, jsfile

def WebView(htmlfile, cssfile, jsfile):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return flask.render_template(htmlfile, cssfile=cssfile, jsfile=jsfile)

    return app

if __name__ == "__main__":
    htmlfile, cssfile, jsfile = VariablestoBoot()

    # Start the Flask app
    flask_app = WebView(htmlfile, cssfile, jsfile)
    flask_app.run(debug=False, host='127.0.0.1', port=8080)
