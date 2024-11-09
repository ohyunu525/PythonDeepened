import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.ensemble import RandomForestClassifier


def predict_windspeed(data):
    dataWind0 = data.loc[data["windspeed"] == 0]
    dataWindNot0 = data.loc[data["windspeed"] != 0]

    wCol = ["season", "weather", "humidity", "month", "temp", "year", "atemp"]

    dataWindNot0["windspeed"] = dataWindNot0["windspeed"].astype("str")

    rfModel_wind = RandomForestClassifier()
    rfModel_wind.fit(dataWindNot0[wCol], dataWindNot0["windspeed"])

    wind0Values = rfModel_wind.predict(X=dataWind0[wCol])

    predictWind0 = dataWind0
    predictWindNot0 = dataWindNot0

    predictWind0["windspeed"] = wind0Values

    data = pd.concat([predictWindNot0, predictWind0])
    data["windspeed"] = data["windspeed"].astype("float")

    data.reset_index(inplace=True)
    data.drop('index', inplace=True, axis=1)

    return data

#ProjectSettings
warnings.filterwarnings('ignore')

mpl.rcParams['axes.unicode_minus'] = False

train = pd.read_csv("../Sources/train.csv", parse_dates=["datetime"])

test = pd.read_csv("../Sources/test.csv", parse_dates=["datetime"])

#train&testIndexing
train["year"] = train["datetime"].dt.year
train["month"] = train["datetime"].dt.month
train["day"] = train["datetime"].dt.day
train["hour"] = train["datetime"].dt.hour
train["minute"] = train["datetime"].dt.minute
train["second"] = train["datetime"].dt.second
train["dayofweek"] = train["datetime"].dt.dayofweek

test["year"] = test["datetime"].dt.year
test["month"] = test["datetime"].dt.month
test["day"] = test["datetime"].dt.day
test["hour"] = test["datetime"].dt.hour
test["minute"] = test["datetime"].dt.minute
test["second"] = test["datetime"].dt.second
test["dayofweek"] = test["datetime"].dt.dayofweek

train = predict_windspeed(train)

fig, ax1 = plt.subplots()
fig.set_size_inches(18, 6)

plt.sca(ax1)
plt.xticks(rotation=30, ha='right')
ax1.set(ylabel='Count', title="train windspeed")
sns.countplot(data=train, x="windspeed", ax=ax1)

plt.savefig("../OutPuts/TrainWindSpeed.png")

#\[T]/
