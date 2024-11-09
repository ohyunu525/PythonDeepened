import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import make_scorer
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import GridSearchCV
from sklearn import metrics


def rmsle(predicted_values, actual_values, convert_exp=True):
    if convert_exp:
        predicted_values = np.exp(predicted_values)
        actual_values = np.exp(actual_values)
    predicted_values = np.array(predicted_values)
    actual_values = np.array(actual_values)

    log_predict = np.log(predicted_values + 1)
    log_actual = np.log(actual_values + 1)
    difference = log_predict - log_actual
    difference = np.square(difference)
    mean_difference = difference.mean()
    score = np.sqrt(mean_difference)

    return score

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

train = pd.read_csv("../../Sources/train.csv", parse_dates=["datetime"])

test = pd.read_csv("../../Sources/test.csv", parse_dates=["datetime"])

pd.options.mode.chained_assignment = None

plt.style.use('ggplot')

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

categorial_feature_names = ["season", "holiday", "workingday", "dayofweek", "weather", "month", "year", "hour"]

for var in categorial_feature_names:
    train[var] = train[var].astype("category")
    test[var] = test[var].astype("category")

feature_names = ["season", "weather", "temp", "atemp", "humidity", "windspeed", "year", "hour", "dayofweek", "holiday", "workingday"]



train = predict_windspeed(train)

X_train = train[feature_names]
X_test = test[feature_names]

label_name = "count"

y_train = train[label_name]

k_fold = KFold(n_splits=10, shuffle=True, random_state=0)

rfModel = RandomForestRegressor(n_estimators=100)

gbm = GradientBoostingRegressor(n_estimators=4000, alpha=0.01)

y_train_log = np.log1p(y_train)

rfModel.fit(X_train, y_train_log)

preds = rfModel.predict(X_train)

score = rmsle(y_train_log, preds)

print("RMSLE Value For Random Forest: ", score)

gbm.fit(X_train, y_train_log)

preds = gbm.predict(X_train)

score = rmsle(y_train_log, preds)

print("RMSLE Value For Gradient Boost: ", score)

predsTest = gbm.predict(X_test)

fig,(ax1,ax2)= plt.subplots(ncols=2)

fig.set_size_inches(12, 5)

sns.distplot(y_train, ax=ax1, bins=50)

sns.distplot(np.exp(predsTest), ax=ax2, bins=50)

plt.savefig("../OutPuts/RmsleValueForRandomForest&GradientBoost.png")

#\[T]/
