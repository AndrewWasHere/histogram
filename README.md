Histogram
=========
A simple web service to show the histogram of inputs. 

Or, a way to make the rolling of d6es (or whatever) over and over again slightly 
more palatable.

Pardon my ugly Javascript. It's not a primary language for me.

Endpoints
---------
/ - Data entry (GET).
/results - Pretty pictures (GET).
/data - data entry (POST), retrieval (GET), and reset (DELETE). Used by the
results endpoint.

Requirements
------------
* [Python](https://python.org) 2.7 or 3.x with [Flask](http://flask.pocoo.org) 0.11.1 or greater.
* [Chart.js](http://www.chartjs.org) 2.1.6 or greater.

Install the Python requirements using pip:

> $ pip install -r requirements.txt

Install Chart.js by copying Chart.bundle.min.js into the static/js directory.

License
-------
This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
[https://opensource.org/licenses/BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)
