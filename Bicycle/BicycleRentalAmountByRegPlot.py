import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import seaborn as sns
from scipy import stats

plt.style.use('ggplot')
mpl.rcParams['axes.unicode_minus'] = False
train = pd.read_csv("./train.csv", parse_dates=["datetime"])

#train["year"] = train["datetime"].dt.year
#train["month"] = train["datetime"].dt.month
#train["hour"] = train["datetime"].dt.hour
#train["day"] = train["datetime"].dt.day
#train["minute"] = train["datetime"].dt.minute
#train["second"] = train["datetime"].dt.second
#train["dayofweek"] = train["datetime"].dt.dayofweek
#print(train["dayofweek"].value_counts())

#corrMatt = train[["temp", "atemp", "casual", "registered", "humidity", "windspeed", "count"]]
#corrMatt = corrMatt.corr()
#print(corrMatt)

#mask = np.array(corrMatt)
#mask[np.tril_indices_from(mask)] = False
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3)
fig.set_size_inches(12, 5)

#sns.heatmap(corrMatt, mask=mask, vmax=8, square=True, annot=True)

sns.regplot(x="temp", y="count", ax=ax1, data=train)
sns.regplot(x="windspeed", y="count", data=train, ax=ax2, color="blue")
sns.regplot(x="humidity", y="count", data=train, ax=ax3, color="purple")
#sns.pointplot(data=train, x="hour", y="count", hue="weather", ax=ax4)
#sns.pointplot(data=train, x="hour", y="count", hue="season", ax=ax5)

#axes[0][0].set(ylabel='Count', title="Rental Amount")
#axes[0][1].set(xlabel='Season', ylabel='Count', title="Rental Amount by Seasons")
#axes[1][0].set(xlabel='Hour Of The Day', ylabel='Count', title="Rental Amount by Hour")
#axes[1][1].set(xlabel='Working Day', ylabel='Count', title="Rental Amount d_on working days")

plt.savefig("BicycleRentalAmountByRegPlot.png")
