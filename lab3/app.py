from flask import Flask, jsonify
from statsGen import statisticsGenerator
import datetime
import sys

# read arguments from command line
args = sys.argv[:]

# get second argument as port
port = args[1]

# initial value of the statistic
startingValue = 1000

# if true the value tends to rise
# if false it tends to fall
increasing = True

# stats generator
statistics = statisticsGenerator(startingValue, increasing)

# create flask app
app = Flask(__name__)


@app.route('/')
def index():
    # serve index.html
    with open("index.html", "r", encoding='utf-8') as f:
        html = f.read()
    return html


@app.route('/background.jpg')
def background():
    # serve background image
    with open("background.jpg", "rb") as f:
        file = f.read()
    return file, 200, [('content-type', 'image/jpg')]


@app.route('/stats')
def stats():
    # return stats as json, with CORS headers
    return jsonify({
        'stats': statistics.get(),
        'time': datetime.datetime.now()
    }), 200, [('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Methods', 'GET')]


# start app
if __name__ == '__main__':
    app.run(port=port, debug=True)
