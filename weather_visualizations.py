import matplotlib.pyplot as plt
import pandas as pd
import datetime
import numpy as np
import sys
import os

df = pd.read_csv(sys.argv[1])
os.makedirs("./visualizations", exist_ok=True)

fig, ax = plt.subplots(figsize=(16, 10), facecolor='white')

for column in df.columns[2:5]:
    plt.plot(df["Date"], df[column], label=column)

plt.ylabel("Temperature (F)")
plt.xlabel("Measurement Date")
plt.title("Temperature from 2024-12-01 to 2025-02-28")
plt.legend()

date = datetime.datetime.strptime(df["Date"][0]," %Y-%m-%d")
end_date = datetime.datetime.strptime(df["Date"].iloc[-1]," %Y-%m-%d")
delta = datetime.timedelta(weeks=1)

x_labels=[]
while date <= end_date:
    x_labels.append(date.strftime("%Y-%m-%d"))
    date += delta

x_ticks = [i for i in range(0, len(df["Date"]),7)]
plt.xticks(x_ticks, x_labels, rotation=45)

plt.savefig("./visualizations/temperature_chart.png")

fig, ax = plt.subplots(figsize=(16, 10), facecolor='white')

precip_df = df[["Date","Condition","Precipitation"]]

rain_mask = precip_df['Condition'].apply(lambda x : x.strip() != "Snowy")
precip_df.insert(1, 'Rain', np.where(rain_mask, precip_df.loc[:,'Precipitation'].copy(), 0.00))
snow_mask = precip_df['Condition'].apply(lambda x : x.strip() == "Snowy")
precip_df.insert(1, 'Snow', np.where(snow_mask, precip_df.loc[:,'Precipitation'].copy(), 0.00))
precip_df

plt.bar(precip_df["Date"], precip_df["Rain"], label="Rain")
plt.bar(precip_df["Date"], precip_df["Snow"], label="Snow", color="lightblue")

plt.ylabel("Precipitation (in)")
plt.xlabel("Measurement Date")
plt.title("Precipitation from 2024-12-01 to present")
plt.legend()

date = datetime.datetime.strptime(df["Date"][0]," %Y-%m-%d")
end_date = datetime.datetime.strptime(df["Date"].iloc[-1]," %Y-%m-%d")
delta = datetime.timedelta(weeks=1)

x_labels=[]
while date <= end_date:
    x_labels.append(date.strftime("%Y-%m-%d"))
    date += delta

x_ticks = [i for i in range(0, len(df["Date"]),7)]
plt.xticks(x_ticks, x_labels, rotation=45)

plt.savefig("./visualizations/precipitation_chart.png")

fig, ax = plt.subplots(figsize=(16, 10), facecolor='white')

plt.plot(df["Date"], df['Wind Speed'], label='Wind Speed')

plt.ylabel("Wind Speed (mph)")
plt.xlabel("Measurement Date")
plt.title("Wind Speeds from 2024-12-01 to present")
plt.legend()

date = datetime.datetime.strptime(df["Date"][0]," %Y-%m-%d")
end_date = datetime.datetime.strptime(df["Date"].iloc[-1]," %Y-%m-%d")
delta = datetime.timedelta(weeks=1)

x_labels=[]
while date <= end_date:
    x_labels.append(date.strftime("%Y-%m-%d"))
    date += delta

x_ticks = [i for i in range(0, len(df["Date"]),7)]
plt.xticks(x_ticks, x_labels, rotation=45)

plt.savefig("./visualizations/wind_speed_chart.png")
