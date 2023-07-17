# Github event monitoring

This application is composed of three main components: a Flask web server, a GitHub API data fetcher service, and a Postgres database. It fetches event data from the GitHub API, stores it in a Postgres database, and provides several API endpoints for analyzing this data.

This will start three containers: a Flask web server (flask-container), a data fetcher service (fetcher-container), and a Postgres database (postgres-container).


## How to run

1. Install the latest Docker distribution for your operating system
2. Clone the repositary and navigate to the repositaries folder
 ```sh
 $ git@github.com:tmachorek/Github-events-monitoring.git && cd Github-events-monitoring
 ```
3. Run the following command (optionally use Docker desktop):
  ```sh
$ docker-compose up
  ```

This will start three containers: a Flask web server (flask-container), a data fetcher service (fetcher-container), and a Postgres database (postgres-container).
This will enable the functionallity of endpoints from the next section.


## API Endpoints

The application provides the following API endpoints:

1. `GET /metrics/average_pr_time?repo_id=<repo_id>` -  Returns the average time between consecutive pull request events for a specific repository with an id of `<repo_id>`.

2. `GET /metrics/event_counts?offset=<offset>` - Returns the number of each type of event that occurred in the last `<offset>` minutes.

3. `GET /metrics/visualization?offset=<offset>` - Returns a bar graph image representing the number of each type of event that occurred in the last `<offset>` minutes.

## C4 L1 Diagram

Following diagram should provide some basics of apps innerworkings.

![image](https://github.com/tmachorek/Github-events-monitoring/assets/129040831/66932490-6e66-4ef1-8775-7208273b91de)
