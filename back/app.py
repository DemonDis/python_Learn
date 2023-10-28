from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def rest_api():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return {
        'request': {
            'name': 'sdfs'
        },
        'request_type': 'auto_test'
    }
    else:
        return 'Content-Type not supported'

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    # app.run(debug=True, host='127.0.0.1', port=3030)