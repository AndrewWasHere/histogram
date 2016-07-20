Histogram
=========
A simple web service to show the histogram of inputs. 

Or, a way to make the rolling of d6es (or whatever) over and over again slightly 
more palatable.

Pardon my ugly Javascript. It's not a primary language for me.

Requirements
------------
* [Python](https://python.org) 2.7 or 3.x with [Flask](http://flask.pocoo.org) 
0.11.1 or greater.
* [Chart.js](http://www.chartjs.org) 2.1.6 or greater.

Install the Python requirements using pip:

> $ pip install -r requirements.txt

Install Chart.js by copying Chart.bundle.min.js into the static/js directory.

Run
---
> $ python histogram.py [--visible] [--port PORT] [--debug]

--visible: Run as host 0.0.0.0. This will allow other machines to see the HTTP
endpoints.

--port PORT: HTTP port to expose. Default is 5000.

--debug: Run in debug mode. See Flask documentation.

Data entry happens at <hostname>:<port>/. Enter a value and click 'Submit' to
add it to the histogram. (The ENTER key should work as the submit button.)

Histogram is displayed at <hostname>:<port>/results. Click the 'Reset' button
to clear the data on the server.

Endpoints
---------
* / - Data entry (GET).
* /results - Pretty pictures (GET).
* /data - data entry (POST), retrieval (GET), and reset (DELETE). Used by the
results endpoint.

License
-------
This software is licensed under the BSD 3-Clause License.
See LICENSE.txt at the root of the project or
[https://opensource.org/licenses/BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)
