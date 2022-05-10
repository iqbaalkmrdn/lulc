# %%
from flask import Flask, request, render_template
import os
import ee
import geemap
import ipywidgets as widgets
from bqplot import pyplot as plt
from ipyleaflet import WidgetControl

import pickle

app = Flask(__name__)

# Fungsi untuk merender main page
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)



