import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import seaborn as sns
from scipy import stats

plt.style.use('ggplot')
mpl.rcParams['axes.unicode_minus'] = False
train = pd.read_csv("../Sources/train.csv", parse_dates=["datetime"])

train["year"] = train["datetime"].dt.year
train["month"] = train["datetime"].dt.month
train["hour"] = train["datetime"].dt.hour
train["day"] = train["datetime"].dt.day
train["minute"] = train["datetime"].dt.minute
train["second"] = train["datetime"].dt.second

figure, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows=2, ncols=3)
figure.set_size_inches(18, 8)

sns.barplot(data=train, x="year", y="count", ax=ax1)
sns.barplot(data=train, x="month", y="count", ax=ax2)
sns.barplot(data=train, x="day", y="count", ax=ax3)
sns.barplot(data=train, x="hour", y="count", ax=ax4)
sns.barplot(data=train, x="minute", y="count", ax=ax5)
sns.barplot(data=train, x="second", y="count", ax=ax6)

ax1.set(ylabel='Count', title="Rental Amount by Year")
ax2.set(xlabel='month', title="Rental Amount by Month")
ax3.set(xlabel='day', title="Rental Amount by Day")
ax4.set(xlabel='hour', title="Rental Amount by Hour")
ax5.set(xlabel='minute', title="Rental Amount by Minute")
ax6.set(xlabel='second', title="Rental Amount by Second")
plt.savefig("../OutPuts/BicycleRentalAmountByYearMonthDayHourMinuteSecondByBarPlot.png")
