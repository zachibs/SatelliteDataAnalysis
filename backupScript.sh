rm -r /root/SATTLA-Data/influxDatabaseBackup/latest_backup
echo "deleted former backup"
influx backup -b SATLLA-2B /root/SATTLA-Data/influxDatabaseBackup/latest_backup
echo "latest backup complete"