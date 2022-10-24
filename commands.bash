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


# Used those links too:
# https://stackoverflow.com/questions/33111835/how-to-set-up-grafana-so-that-no-password-is-necessary-to-view-dashboards
# https://askubuntu.com/questions/256782/how-to-copy-paste-contents-in-the-vi-editor
# https://docs.influxdata.com/influxdb/cloud/reference/cli/influx/backup/#works-with-influxdb-oss-2x

# update the influx cli config:
# influx config set -n satconfig -u http://ipaddress:8086

# backup data:
# Use backupScript.sh
# move data to local: scp root@ipaddress:SATTLA-Data/influxDatabaseBackup/latest_backup/* .