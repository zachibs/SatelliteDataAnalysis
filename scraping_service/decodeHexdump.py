import pandas as pd

timestamp = 1642087950
timeloop = 67.8

type_becon = 0x00
type_echo = 0x01
type_ack = 0x02
type_range = 0x03
type_rpi = 0x04
type_text = 0x05
type_sbeacon = 0x06
type_command = 0x07
type_setting = 0x08
type_none = 0x09
type_mv = 0x0A
type_ld = 0x0B
type_rng = 0x0C

col_names_srt_bcn = [
    "local_address",
    "sd_outbox",
    "msg_type",
    "msg_received",
    "msg_index",
    "battery_volts",
    "battery_current",
    "sns_ntc1",
    "sns_ntc2",
]


def decode_srt_bcn(data):
    df = dict.fromkeys(col_names_srt_bcn)
    if len(data) > 0:
        df['local_address'] = [hex(data[0])]
        df['sd_outbox'] = [data[1]]
        df['msg_type'] = [data[2]]
        df['msg_received'] = [data[3]]
        df['msg_index'] = [str(int.from_bytes(
            data[4:6], byteorder='little', signed=False))]
        df['battery_volts'] = [str(int.from_bytes(
            data[6:8], byteorder='little', signed=False))]
        df['battery_current'] = [str(int.from_bytes(
            data[8:10], byteorder='little', signed=True))]
        df['sns_ntc1'] = [str(int.from_bytes(
            data[10:11], byteorder='little', signed=True))]
        df['sns_ntc2'] = [str(int.from_bytes(
            data[11:12], byteorder='little', signed=True))]

    df = pd.DataFrame.from_dict(df)
    return df


def decode_lng_bcn(data):
    df = dict()
    if len(data) > 0:
        df['local_address'] = hex(data[0])
        df['destination'] = hex(data[1])
        df['msg_type'] = data[2]
        df['msg_size'] = data[3]
        df['msg_index'] = str(int.from_bytes(
            data[4:6], byteorder='little', signed=False))
        df['msg_time'] = str(int.from_bytes(
            data[6:8], byteorder='little', signed=False))
        df['msg_ack_req'] = data[8]

        if len(data) > 10:  # payload
            df['gps_month'] = data[9]
            df['gps_day'] = data[10]
            df['gps_hour'] = data[11]
            df['gps_min'] = data[12]

            df['gps_lat'] = str(float(int.from_bytes(
                data[13:17], byteorder='little', signed=True)) / 1000)
            df['gps_lng'] = str(float(int.from_bytes(
                data[17:21], byteorder='little', signed=True)) / 1000)
            df['gps_alt'] = str(int.from_bytes(
                data[21:23], byteorder='little', signed=False) / 1000)
            df['gps_speed'] = str(int.from_bytes(
                data[23:25], byteorder='little', signed=False))
            df['gps_course'] = str(int.from_bytes(
                data[25:27], byteorder='little', signed=False))
            df['gps_sat'] = data[27]

            df["sns_gx"] = str(int.from_bytes(
                data[29:31], byteorder='little', signed=True) / 100)
            df["sns_gy"] = str(int.from_bytes(
                data[31:33], byteorder='little', signed=True) / 100)
            df["sns_gz"] = str(int.from_bytes(
                data[33:35], byteorder='little', signed=True) / 100)
            df["sns_mx"] = str(int.from_bytes(
                data[35:37], byteorder='little', signed=True) / 100)
            df["sns_my"] = str(int.from_bytes(
                data[37:39], byteorder='little', signed=True) / 100)
            df["sns_mz"] = str(int.from_bytes(
                data[39:41], byteorder='little', signed=True) / 100)
            df["sns_bmp_temp_c"] = str(int.from_bytes(
                data[41:43], byteorder='little', signed=True) / 100)
            df['sns_ntc1'] = str(int.from_bytes(
                data[43:44], byteorder='little', signed=True))
            df['sns_ntc2'] = str(int.from_bytes(
                data[44:45], byteorder='little', signed=True))

            df["battery_soc"] = str(int.from_bytes(
                data[45:46], byteorder='little', signed=True))
            df["battery_health"] = str(int.from_bytes(
                data[46:47], byteorder='little', signed=True))
            df["battery_volts"] = str(int.from_bytes(
                data[47:49], byteorder='little', signed=False))
            df["battery_current"] = str(int.from_bytes(
                data[49:51], byteorder='little', signed=True))
            df["battery_full_capacity"] = str(int.from_bytes(
                data[51:53], byteorder='little', signed=False))
            df["battery_capacity"] = str(int.from_bytes(
                data[53:55], byteorder='little', signed=False))
            df["battery_power"] = str(int.from_bytes(
                data[55:57], byteorder='little', signed=True))

            df["sd_outbox"] = data[57]
            df["sd_sent"] = data[58]
            df["sd_rpi"] = data[59]
            df["sd_files"] = data[60]
        return df


def decode(encoded_data):
    id = encoded_data[2]
    if id == type_becon:
        return decode_lng_bcn(encoded_data)
    elif id == type_sbeacon:
        return decode_srt_bcn(encoded_data)
    else:
        print(f'Unidentified ID: {id}')
        return ''
