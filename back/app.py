from flask import Flask, request, render_template, Response
from flask_cors import CORS
import psycopg2
from password import DB_CONNECT_LOCAL
from datetime import datetime
import time

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

status = {}

@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def rest_api():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        if json['request_type'] == 'posts':
            cursor.execute("SELECT plan_id FROM plans")
            all_plans = cursor.fetchall()
            return {
            'request': {
                'name': all_plans
            },
            'request_type': 'posts'
        }
        if json['request_type'] == 'add_posts':
            cursor.execute("INSERT INTO plans(plan_id, plan_parent_id, plan_stage_id) VALUES ('TEST1', 'TEST1', 'TEST1');")
            connection.commit()
            status["message"] = 'update'
            time.sleep(1)
            status["message"] = 'empty'
            return {
            'request': {
                'posts': 'ADD'
            },
            'request_type': 'add_posts'
        }
        if json['request_type'] == 'del_posts':
            cursor.execute("DELETE from plans Where plan_id='TEST1'")
            connection.commit()
            status["message"] = 'delete'
            time.sleep(1)
            status["message"] = 'empty'
            return {
            'request': {
                'posts': 'DELL'
            },
            'request_type': 'del_posts'
        }
    else:
        return 'Content-Type not supported'
    

@app.route('/sse')
def sse():
    def sse_events():
        status['message'] = ''
        while True:
            yield "data: {}\n\n".format(status['message'])
            time.sleep(1)

    return Response(sse_events(), mimetype="text/event-stream")
if __name__ == "__main__":
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True, host='127.0.0.1', port=3030)