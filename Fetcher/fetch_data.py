import os
import time

import requests
import psycopg2

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

while True:
    print("Fetching data into PostgrSQL db.")
    response = requests.get('https://api.github.com/events')
    events = response.json()

    for event in events:
        if event['type'] in ['WatchEvent', 'PullRequestEvent', 'IssuesEvent']:
            insert = "INSERT INTO GITHUB_EVENTS (repo_id, event_type, event_timestemp) VALUES (%s, %s, %s)"
            cur.execute(insert, (event['repo']['id'], event['type'], event['created_at']))
    conn.commit()
    time.sleep(60)