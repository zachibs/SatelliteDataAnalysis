# Satellite Data Visualization

A project to scrape satellite data from tinygs and clean it, storing it in a pandas dataframe and then pushing it to an influxdb database. visualizing the data in grafana.
where everything is containerized as services using docker compose: first is influxdb, second is grafana, and the third is a service for scraping and sending data to influxdb.

## How to setup:

**prerequisites:**

1. docker
2. docker-compose

**Setup:**

1. git clone https://github.com/zachibs/satellite_data_services
2. docker-compose up
3. go to http://ipaddress:3000
4. set up influxdb as datasource as shown below:
5. import the grafana-dashboard.json file in the dashboard import tab

**Settings up influxdb as a data source in grafana:**

1. set query as flux
2. set url to - ip:8086
3. use basic auth and with credentials
4. use header = token, value = DOCKER_INFLUXDB_INIT_ADMIN_TOKEN
5. db details:
   - organization=DOCKER_INFLUXDB_INIT_ORG
   - token=DOCKER_INFLUXDB_INIT_ADMIN_TOKEN
   - default Bucket=DOCKER_INFLUXDB_INIT_BUCKET

## TODO's

- TODO: refactor the codebase(better variable names, cleaner code)
- TODO: figure out how to create data source by code
- TODO: figure out how to create dashboard by code (import json model)
- TODO : visualize the satellite location: using sgp4 - library for getting satellite location by two numbers
