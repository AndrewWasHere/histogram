"""
Copyright 2016, Andrew Lin
All rights reserved.

This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
https://opensource.org/licenses/BSD-3-Clause
"""
import collections
import json
import os

import flask


app = flask.Flask(__name__)
histogram = None


def empty_histogram():
    """Returns an empty histogram."""
    return collections.defaultdict(int)


def modify_data_redirect_endpoint():
    """Common redirect endpoint when modifying data."""
    url = flask.url_for('index')
    return flask.redirect(url)


@app.route('/')
def index():
    """Serve main endpoint."""
    return app.send_static_file('index.html')


@app.route('/js/<path:path>')
def send_js(path):
    """Serve javascript."""
    return flask.send_from_directory(os.path.join('static', 'js'), path)


@app.route('/results')
def results():
    """Serve results endpoint."""
    return app.send_static_file('results.html')


@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def data():
    """Serve data endpoint."""
    global histogram
    request = flask.request

    if request.method == 'GET':
        return json.dumps(histogram)

    elif request.method == 'POST':
        key = flask.request.form['value']
        histogram[key] += 1
        return modify_data_redirect_endpoint()

    elif request.method == 'DELETE':
        histogram = empty_histogram()
        return modify_data_redirect_endpoint()


if __name__ == '__main__':
    histogram = empty_histogram()
    app.run()
