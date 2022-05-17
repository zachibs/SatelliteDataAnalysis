# satellite_data_services

## Introduction:

A project to scrape satellite data from tinygs and clean it, storing it in a pandas dataframe and then pushing it to an influxdb database. then visualizing the data in grafana.
where everything is containerized as services using docker compose: first is influxdb, second is grafana, and the third is a service for scraping and sending data to influxdb.

**TODO List:**

- TODO: figure out how to pull long beacons data too and push it to influxdb
- TODO: change inside the push function, the way of generating the data to push. instead of from a csv file, use the generate method directly.
- TODO: figure out how to create dashboard by code (import json model)
- TODO: check prometheus python api
- TODO: check self hosting on grafana
- TODO: check csv plugin for grafana

**TODO's To Consider:**

- TODO: create the dataframe_to_points function (in debate if should)

**Visualization in grafana should look like:**

1. show last packet id
2. last message index
3. last message received
4. state_plot_power_V() ----- gauge (0 - 4.2) min 3.2 (0 - 3.2 red, 3.2 - 3.79 orange, 3.8 - 4.2 green)
5. state_plot_power_mA() --- gauge (-1000 0 500) (neg - usage - show as red, pos - charging - show as green)
6. state_plot_temp() ------ 2 graph - ntc1 , ntc2 (over time)
7. state_plot_gyro()
8. tate_plot_mag()

**Future TODO's:**

- TODO : visualize the satellite location: using sgp4 - library for getting satellite location by two numbers
- TODO : push the project to a web app in azure using an account with my ms mail

**Settings up influxdb as a data source in grafana:**

1. set query as flux
2. set url to - ip:8086
3. use basic auth and with credentials
4. use header = token, value = DOCKER_INFLUXDB_INIT_ADMIN_TOKEN
5. db details:
   - organization=DOCKER_INFLUXDB_INIT_ORG
   - token=DOCKER_INFLUXDB_INIT_ADMIN_TOKEN
   - default Bucket=DOCKER_INFLUXDB_INIT_BUCKET
