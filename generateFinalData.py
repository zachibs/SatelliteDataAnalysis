from generateUrlDf import generateURLDataFrame
from decodeHexdump import decode
import pandas as pd


# Generating a final dataframe contaning last telemetries with timestamps
def generate(numOfValues):
    dfURLs = generateURLDataFrame(numOfValues)
    df = pd.DataFrame()

    for index in range(len(dfURLs)):
        hexdump = bytearray.fromhex(dfURLs.iloc[index]['hexdump'])
        tempDF = decode(hexdump)
        if (type(tempDF) is dict):
            continue
        tempDF.insert(0, "timestamp", [dfURLs.iloc[index]["date-time"]])
        df = pd.concat([tempDF, df])

    df = df.iloc[::-1]
    df.reset_index(inplace=True)
    df.drop("index", axis=1, inplace=True)
    df.to_csv("generatedCSVs/GeneratedData.csv", encoding='utf-8')
    return df


def generateFinalData():
    values_wanted = int(input("how many values do you want to get?: \n"))
    return generate(values_wanted)
