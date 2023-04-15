# SatelliteDataAnalysis


## Introduction
A project to scrape satellite data from tinygs and clean it, storing it in a pandas dataframe and then pushing it to an influxdb database. visualizing the data in grafana.
where everything is containerized as services using docker compose: first is influxdb, second is grafana, and the third is a service for scraping and sending data to influxdb.

## prerequisites:

* docker
* docker-compose

## Setup:

1. `git clone https://github.com/zachibs/SatelliteDataAnalysis.git`
2. `cd scarping_service`
2. `docker-compose up`
3. Go to `http://LocalIPAddress:3000`
4. Set up InfluxDB as a data source in Grafana:
>  1. Go to Configuration -> Data sources -> Add data source
>  2. Select InfluxDB
>  3. Set query as flux
>  4. Set `URL=http://LocalIPAddress:8086`
>  5. Select basic auth and with credentials
>  6. Set `User=DOCKER_INFLUXDB_INIT_USERNAME`, `Password=DOCKER_INFLUXDB_INIT_PASSWORD`
>  7. Click on Custom HTTP Headers -> Add header
>  8. Set `Header=token`, `Value=DOCKER_INFLUXDB_INIT_ADMIN_TOKEN`
>  9. InfluxDB Details:
>     - `organization=DOCKER_INFLUXDB_INIT_ORG`
>     - `token=DOCKER_INFLUXDB_INIT_ADMIN_TOKEN`
>     - `default Bucket=DOCKER_INFLUXDB_INIT_BUCKET`
>  10. Click on 'Save & test'

6. Go to Dashboards -> Import
7. Click on 'Upload dashboard JSON file'
8. import the 'grafana-dashboard.json' file found in the repository directory
9. Update each panel datasource to the correct one
> 1. Click on a panel -> Edit
> 2. Select Data source to InfluxDB
> 3. Click on Query inspector
> 4. Click on Refresh
> 5. Click on Apply
