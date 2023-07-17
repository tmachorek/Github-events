import os

import matplotlib.pyplot as plt
import psycopg2

from flask import send_file
from io import BytesIO
from flask import Flask, request

app = Flask(__name__)

if os.getenv('RUNNING_IN_DOCKER') is not None:
    host = "postgres"
else:
    host = "localhost"

conn = psycopg2.connect(
    host=host,
    database="postgres",
    user="postgres",
    password="postgre",
    port="5432"
)

cur = conn.cursor()


@app.route('/metrics/average_pr_time', methods=['GET'])
def average_pr_time():
    repo_id = request.args.get('repo_id')
    query = "SELECT AVG(time_to_sec(TIMEDIFF(event_timestemp, LAG(event_timestemp) OVER (ORDER BY event_timestemp)))) "\
        "FROM GITHUB_EVENTS "\
        "WHERE event_type = 'PullRequestEvent' AND repo_id = %s"

    cur.execute(query, (repo_id,))

    average_time = cur.fetchone()[0]

    return {'average_time': average_time}


@app.route('/metrics/event_counts', methods=['GET'])
def event_counts():
    offset = int(request.args.get('offset'))

    query = "SELECT event_type, COUNT(*) " \
        "FROM GITHUB_EVENTS " \
        "WHERE event_timestemp > NOW() - INTERVAL '%s minutes' "\
        "GROUP BY event_type"

    cur.execute(query, (offset,))

    counts = cur.fetchall()
    return {event_type: count for event_type, count in counts}


@app.route('/metrics/visualization', methods=['GET'])
def visualization():
    offset = int(request.args.get('offset'))
    query = "SELECT event_type, COUNT(*) " \
        "FROM GITHUB_EVENTS " \
        "WHERE event_timestemp > NOW() - INTERVAL '%s minutes' " \
        "GROUP BY event_type"

    cur.execute(query, (offset,))

    counts = cur.fetchall()

    event_types, event_counts = zip(*counts)
    plt.bar(event_types, event_counts)
    plt.xlabel('Event Type')
    plt.ylabel('Count')
    plt.title(f'Event Counts in Last {offset} Minutes')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')


if __name__ == '__main__':
    if os.getenv('RUNNING_IN_DOCKER') is not None:
        address = "0.0.0.0"
    else:
        address = "127.0.0.1"

    app.run(host=address, port=8080)