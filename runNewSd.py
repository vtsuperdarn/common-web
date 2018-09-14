from flask import Flask, render_template, request, jsonify
import os
import sys
import datetime

app = Flask(__name__)

@app.route("/")
def starter():
    return render_template('index.html')

@app.route("/histindexpage")
def generate_base_page():
    return render_template('hist_sctr.html')    

if __name__ == "__main__":
    app.debug=True
    app.run(host= '0.0.0.0',port=5001, threaded=True)