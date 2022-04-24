# https://thedatafrog.com/en/articles/docker-influxdb-grafana/
# https://www.youtube.com/watch?v=NOWoLfpY2kE&ab_channel=Thetips4you


# ssh into cli
docker exec -it influxdb sh

# to stop the cluster:
docker-compose stop

# to start the cluster again:
docker-compose start

# --------------------------------------------------------------------------------------------
# First Time Setup:
# settings up influxdb
docker pull influxdb

# settings up grafna
docker pull grafana/grafana

# clean docker enviorment
docker system prune -a --volumes

# install docker compose
pip install docker-compose

# compose the volume (docker-compoes file need to be in the terminal location)
docker-compose up -d

# go to http://ipaddress:3000 for grafana
# go to http://ipaddress:8086 for influxdb
# connect grafana to influxdb with the next link:
# http://wiki.webperfect.ch/index.php?title=InfluxDB_2.x:_Error:_Bad_Request_(Grafana_and_InfluxQL)&oldid=2578
# ------------------------------------------------------------------------------------------------
