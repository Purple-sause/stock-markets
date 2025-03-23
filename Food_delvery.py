from  google_play_scraper import app
import pandas as pd
from datetime import datetime
import time

df= pd.read_csv("./apps.csv")
df['appID'] = df['appID'].str.strip()
def app_tilegiver():
    df["title"] = [app(i, lang="en", country="us")["title"] for i in df["appID"]]
    print(df)
    df.to_csv("./apps.csv",index=False)
    time.sleep(3)

#app_tilegiver()

def Appdwld_tracker():
    now=datetime.now().strftime("%Y-%m-%d %H")
    df[f"Dwnl {now}"] = [app(i, lang="en", country="us")["realInstalls"] for i in df["appID"]]
    print(df)
    df.to_csv("./apps.csv",index=False)
    time.sleep(2)

Appdwld_tracker()