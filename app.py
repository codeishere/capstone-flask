from flask import Flask, render_template
import os, sys

app = Flask(__name__)

@app.route("/")
def hello():
    appversion = os.environ['APP_VERSION']
    return render_template('index.html', version=appversion)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
