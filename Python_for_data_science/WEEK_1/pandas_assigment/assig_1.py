import pandas as pd
import numpy as np
import geopy as gp

data = pd.read_csv("201809-citibike-tripdata.csv")
cols = data.columns
data.columns = cols.map(lambda x: x.replace(" ", "_") if isinstance(x, (str)) else x)
# print(data.columns)
# print(np.median(data["tripduration"]))
# print(data.where("start station name" == "end station name"))
# print(data.query("start_station_name == end_station_name").count())
# print(data["bikeid"].value_counts())
# print(data.groupby(["usertype"])[["tripduration"]].mean() / 60)
# print(data["tripduration"].mean() / 60)
print(data.groupby(["bikeid"])[["tripduration"]].max())
data["starttime"] = pd.to_datetime(data["starttime"])
data["stoptime"] = pd.to_datetime(data["stoptime"])
# dist = data.query(
#     "starttime >= time(2018-09-01 06:00:00) and stoptime <= time(2018-09-01 10:00:00)"
# )
print(data["start_station_id"].isnull())
x = data[
    (data["starttime"] > "2018-09-01 18:00:00")
    & (data["stoptime"] <= "2018-09-01 20:00:00")
]
# print(x["start_station_id"][3394.0].value_counts())
print(x.query("start_station_id == 3394.0")["start_station_id"].value_counts())

# print(data)
