from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from datetime import datetime
import pandas as pd


col_names = [
    "url",
    "label",
    "msg_index",
    "msg_type",
    "received_date",
    "received_time",
    "num_os_stations",
    "station_names",
    "station_dists",
    "station_times"
    "hexdump"
]


# Getting a list of links from the site
def urlsGenerator():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get("https://tinygs.com/satellite/SATLLA-2B")
    driver.implicitly_wait(220)
    time.sleep(4)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    link_list = []
    for link in soup.find_all(class_='pa-7 clickable v-card v-card--link v-sheet theme--light'):
        link_list.append(f"https://tinygs.com{(link.get('href'))}")
    driver.close()
    return link_list


# Traveling to each new link and getting data
def getData(url):
    s = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(220)
    time.sleep(4)
    df = dict.fromkeys(col_names)

    df['url'] = [url]
    df['label'] = [driver.find_elements(
        by=By.XPATH, value='//h1[@class="ma-2 mb-5"]')[0].text]
    received_on = driver.find_elements(
        by=By.XPATH, value='//h1[@class="ma-2 mb-5"]//following::div[1]')[0].text
    received_date = datetime.strptime(received_on.split(
        ':', 1)[1].strip(), '%B %d, %Y %I:%M %p')
    df['received_date'] = [received_date.strftime("%m/%d/%Y")]
    df['received_time'] = [received_date.strftime("%H:%M:%S")]
    num_os_stations = len(driver.find_elements(
        by=By.XPATH, value='//h3[@class="caption grey--text"]'))
    df['num_os_stations'] = [num_os_stations]
    station_names_e = driver.find_elements(
        by=By.XPATH, value='//h3[@class="caption grey--text"]//following::div[1]//strong')
    station_dist_e = driver.find_elements(by=By.XPATH,
                                          value='//h3[@class="caption grey--text"]//following::div[4]')
    station_time_e = driver.find_elements(by=By.XPATH,
                                          value='//h3[@class="caption grey--text"]//following::div[10]')
    station_names = ''
    for name_element in station_names_e:
        station_names += name_element.text.split(' ', maxsplit=1)[1] + ','
    df['station_names'] = [station_names]
    station_dists = ''
    for dist_element in station_dist_e:
        station_dists += dist_element.text.split()[0] + ','
    df['station_dists'] = [station_dists]
    station_times = ''
    for time_element in station_time_e:
        station_times += time_element.text + ','
    df['station_times'] = [station_times]
    hexdump = driver.find_elements(
        by=By.XPATH, value='//pre[@class="hexdump"]')[0].text
    lines = hexdump.split('\n')
    hexdump_str = ''
    for i, line in enumerate(lines):
        if i == 0:
            continue
        hexdump_str += ''.join(line.split(' ')[1:10])
    df['hexdump'] = [hexdump_str]
    df['msg_index'] = [int.from_bytes(bytearray.fromhex(
        hexdump_str[8:12]), byteorder='little', signed=False)]
    df['msg_type'] = [int.from_bytes(bytearray.fromhex(
        hexdump_str[4:6]), byteorder='little', signed=False)]

    df = df = pd.DataFrame.from_dict(df)
    return df


# Generating a dataframe with all the links and metadata
def generateURLDataFrame(limit):
    url_list = urlsGenerator()
    count = 0
    for url in url_list:
        if (count == 0):
            df = getData(url)
            count += 1
        else:
            tempDF = getData(url)
            df = pd.concat([df, tempDF])
            count += 1

        if(count >= limit):
            break

    df['date_time'] = df['received_date'] + " " + df['received_time']
    dates = pd.to_datetime(df['date_time'])
    df['timestamp'] = dates
    df = df.sort_values(by=['timestamp'], ascending=True)
    df.drop("date_time", axis=1, inplace=True)
    time_stamp_column = df.pop('timestamp')
    df.insert(0, "date-time", time_stamp_column)
    df = df.iloc[::-1]
    df.to_csv("generatedCSVs/generatedCSVFile.csv", encoding='utf-8')
    return df
