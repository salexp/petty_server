from flask import Flask, Response
from flask import json, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello_world():
    return Response(
        'Hello world from Flask!\n',
        mimetype='text/plain'
    )


@app.route('/hello/<req_id>')
def hello_world_id(req_id):
    return Response(
        'Hello {} world from Flask!\n'.format(req_id),
        mimetype='text/plain'
    )


@app.route('/messages', methods=['POST'])
def api_message():
    if request.content_type == 'text/plain':
        return "Text Message: " + request.data
    elif request.content_type == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    else:
        return "415 Unsupported Media Type"


if __name__ == '__main__':
    app.run()
