# satellite_data_services

## Introduction:

A project to scrape satellite data from tinygs and clean it, storing it in a pandas dataframe and then pushing it to an influxdb database. then visualizing the data in grafana.
where everything is containerized as services using docker compose: first is influxdb, second is grafana, and the third is a service for scraping and sending data to influxdb.

TODO List:

- TODO: enhance the function that writes the data to influxdb
- TODO: figure out how to pull long beacons data too and push it to influxdb
- TODO: replace writing to influxdb, instead of from csv, use the generate method from generateFinalData
- TODO: create a requirements.txt file
- TODO: create a docker image for 'scarping writing to database service'

Visualization in grafana should look like:

1. show last packet id
2. last message index
3. last message received
4. state_plot_power_V() ----- gauge (0 - 4.2) min 3.2
5. state_plot_power_mA() --- gauge (-1000 0 500) (neg - usage, pos - charging)
6. state_plot_temp() ------ 2 graph - ntc1 , ntc2 (over time)
7. state_plot_gyro()
8. tate_plot_mag()

Future TODO's:

- TODO : visualize the satellite location: using sgp4 - library for getting satellite location by two numbers
- TODO : push the project to a web app in azure using an account with my ms mail
