from urllib.request import urlopen
import json
import pandas as pd
import os

def retreive_data():
  if(not os.path.exists("data")):
    os.makedirs("data")
  response = urlopen("https://api.openf1.org/v1/drivers")
  data = json.loads(response.read().decode("utf-8"))

  # save to csv
  df = pd.DataFrame(data)
  df.to_csv("data/drivers.csv", index=False)

retreive_data()
df = pd.read_csv("data/drivers.csv")
print(df.iloc[df["broadcast_name"] == "M VERSTAPPEN"]["driver_number"])
