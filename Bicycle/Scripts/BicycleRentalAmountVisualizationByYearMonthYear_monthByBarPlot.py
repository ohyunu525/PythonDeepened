import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import seaborn as sns
from scipy import stats


def concatenate_year_month(datetime):
    return "{0}-{1}".format(datetime.year, datetime.month)


plt.style.use('ggplot')
mpl.rcParams['axes.unicode_minus'] = False
train = pd.read_csv("../Sources/train.csv", parse_dates=["datetime"])

train["year"] = train["datetime"].dt.year
train["month"] = train["datetime"].dt.month
train["hour"] = train["datetime"].dt.hour
train["day"] = train["datetime"].dt.day
train["minute"] = train["datetime"].dt.minute
train["second"] = train["datetime"].dt.second
train["dayofweek"] = train["datetime"].dt.dayofweek

train["year_month"] = train["datetime"].apply(concatenate_year_month)

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
fig.set_size_inches(18, 4)

sns.barplot(data=train, x="year", y="count", ax=ax1)
sns.barplot(data=train, x="month", y="count", ax=ax2)

plt.savefig("../OutPuts/BicycleRentalAmountByYearMonthByBarPlot.png")

fig, ax3 = plt.subplots(nrows=1, ncols=1)
fig.set_size_inches(18, 4)

sns.barplot(data=train, x="year_month", y="count", ax=ax3)

plt.savefig("../OutPuts/BicycleRentalAmountByYear+MonthByBarPlot.png")
