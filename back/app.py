from flask import Flask, request, render_template
from flask_cors import CORS
import psycopg2
from password import DB_CONNECT_LOCAL

connection = psycopg2.connect(
    user=DB_CONNECT_LOCAL.get("user"),
    password=DB_CONNECT_LOCAL.get("password"),
    host=DB_CONNECT_LOCAL.get("host"),
    port=DB_CONNECT_LOCAL.get("port"),
    database=DB_CONNECT_LOCAL.get("database")
)
cursor = connection.cursor()

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def rest_api():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        print('!!!!! !!!', json['request_type'])
        cursor.execute("SELECT * FROM plans")
        record = cursor.fetchall()
        print('!!!!!', record)
        return {
        'request': {
            'name': 'hi!'
        },
        'request_type': 'auto_test'
    }
    else:
        return 'Content-Type not supported'

if __name__ == "__main__":
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True, host='127.0.0.1', port=3030)