# Used this article to construct this script:
# https://www.influxdata.com/blog/getting-started-with-python-and-influxdb-v2-0/

# TODO need to write a function that takes a df and create Point objects from it

from multiprocessing.connection import Client
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
import socket


# Get local ip
hostname = socket.gethostname()
IP = f"{socket.gethostbyname(hostname)}:8086"

# Connect to influxdb using the credentials in the docker-compose file
client = InfluxDBClient(url=IP, token="123456789", org="influx")

# creating api's for write and read:
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

# Experementing with queries and writes
p = Point("my_measurement").tag(
    "location", "Prague").field("temperature", 28.3)

write_api.write(bucket="influx", record=p)

result = query_api.query('from(bucket:"influx") |> range(start: -10m)')

for table in result:
    print(f"Table: {table} \n")
    for record in table.records:
        print(f"Row: {record.values} \n")

client.close()
