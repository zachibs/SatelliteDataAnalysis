# Used this article to construct this script:
# https://www.influxdata.com/blog/getting-started-with-python-and-influxdb-v2-0/

# TODO need to write a function that takes a df and create Point objects from it

from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import socket
import pandas as pd
from generateFinalData import generate
from datetime import datetime


def write_to_db_short(columns_list, column_to_write, data, write_api):
    columns_list.remove(column_to_write)
    data_without_column = data.drop(columns_list, axis=1, inplace=False)
    columns_list.append(column_to_write)
    write_api.write("SATLLA-2B", record=data_without_column,
                    data_frame_measurement_name=column_to_write)


def write_to_db_long(columns_list, column_to_write, long_data, write_api):
    columns_list.remove(column_to_write)
    data_only_column = long_data.drop(columns_list, axis=1, inplace=False)
    columns_list.append(column_to_write)
    write_api.write("SATLLA-2B", record=data_only_column,
                    data_frame_measurement_name=column_to_write)


def push_to_db():
    # Get local ip

    # when used outside the container
    # hostname = socket.gethostname()
    # IP = f"{socket.gethostbyname(hostname)}:8086"

    # when used inside the container
    IP = "http://influxdb:8086"
    print(IP)

    # Connect to influxdb using the credentials in the docker-compose file
    client = InfluxDBClient(url=IP, token="123456789", org="influx")

    # creating APIs:
    write_api = client.write_api(write_options=SYNCHRONOUS)
    delete_api = client.delete_api()
    query_api = client.query_api()
    bucket_api = client.buckets_api()

    # Creating the SATLLA bucket if its not been created yet
    try:
        bucket_api.create_bucket(bucket_name="SATLLA-2B")
    except:
        pass
    # bucket_api.delete_bucket(bucket_api.find_bucket_by_name("SATLLA-2B"))

    # generating the data
    generate()
    data = pd.read_csv("generatedCSVs/GeneratedData.csv")
    data.drop("Unnamed: 0", axis=1, inplace=True)
    three_hours_nanoseconds = 0
    # three_hours_nanoseconds = 10800000000000  # when used outside container
    data["timestamp"] = data["timestamp"].apply(
        lambda x: pd.to_datetime(x).value - three_hours_nanoseconds)
    data["battery_volts"] = data["battery_volts"].apply(
        lambda x: x/1000)
    first_row = data.iloc[0:1]  # capturing the latest telemetry
    first_row.set_index("timestamp", inplace=True)
    data.set_index("timestamp", inplace=True)

    # deleting former latest telemetry (if exists) and writing the new latest
    start = "1970-01-01T00:00:00Z"
    stop = f"{datetime.now().date()}T23:59:00Z"
    try:
        delete_api.delete(
            start, stop, '_measurement="latest"', bucket="SATLLA-2B")
    except:
        pass
    write_api.write("SATLLA-2B", record=first_row, data_frame_measurement_name="latest",
                    data_frame_tag_columns=["msg_type"])

    # Writing the data

    columns_list = ["local_address", "sd_outbox", "msg_type", "msg_index", "battery_volts", "battery_current", "sns_ntc1",
                    "sns_ntc2", "destination", "msg_size", "msg_time", "msg_ack_req", "gps_month",
                    "gps_day", "gps_hour", "gps_min", "gps_lat", "gps_lng", "gps_alt", "gps_speed",
                    "gps_course", "gps_sat", "sns_gx", "sns_gy", "sns_gz", "sns_mx", "sns_my",
                    "sns_mz", "sns_bmp_temp_c", "battery_soc", "battery_health", "battery_full_capacity",
                    "battery_capacity", "battery_power", "sd_sent", "sd_rpi", "sd_files"]

    short_data_name_list = ["battery_volts",
                            "battery_current", "sns_ntc1", "sns_ntc2"]

    long_data_name_list = ["sns_bmp_temp_c", "sns_mx",
                           "sns_my", "sns_mz", "sns_gx", "sns_gy", "sns_gz"]

    for column in short_data_name_list:
        write_to_db_short(columns_list, column, data, write_api)

    long_data = data.dropna(inplace=False)

    for column in long_data_name_list:
        write_to_db_long(columns_list, column, long_data, write_api)

    client.close()
