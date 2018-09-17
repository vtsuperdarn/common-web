from flask import Flask, render_template, request, jsonify
import os
import sys
import datetime

app = Flask(__name__)

@app.route("/")
def starter():
    return render_template('index.html')

@app.route("/rt_display")
def generate_rt_display_page():
    return render_template('rt_display.html')  

@app.route("/rt_conv")
def generate_rt_conv_page():
    return render_template('rt_conv.html')        

@app.route("/rt_dscvr")
def generate_rt_dscvr_page():
    return render_template('rt_dscvr.html')  

if __name__ == "__main__":
    app.debug=True
    app.run(host= '0.0.0.0',port=5001, threaded=True)