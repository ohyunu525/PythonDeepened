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

train = pd.read_csv("../Sources/train.csv", parse_dates=["datetime"])

test = pd.read_csv("../Sources/test.csv", parse_dates=["datetime"])

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

ridge_m_ = Ridge()

alpha = 1/np.array([0.01, 0.1, 1, 2, 3, 4, 10, 30, 100, 200, 300, 400, 800, 900, 1000])

ridge_params_ = {'max_iter': [3000], 'alpha': alpha}

rmsle_scorer = metrics.make_scorer(rmsle, greater_is_better=False)

grid_ridge_m = GridSearchCV(ridge_m_, ridge_params_, scoring=rmsle_scorer, cv=5)

y_train_log = np.log1p(y_train)

grid_ridge_m.fit(X_train, y_train_log)

preds = grid_ridge_m.predict(X_train)

print(grid_ridge_m.best_params_)

print("RMSLE Value For Ridge Regression: ", rmsle(y_train_log, preds))

df = pd.DataFrame(grid_ridge_m.cv_results_)

df["alpha"] = df["params"].apply(lambda x: x["alpha"])
df["rmsle"] = df["mean_test_score"].apply(lambda x: -x)

fig, ax = plt.subplots()
fig.set_size_inches(12, 5)
plt.xticks(rotation=30, ha='right')
sns.pointplot(data=df, x="alpha", y="rmsle", ax=ax)
plt.savefig("../OutPuts/RmsleValueForRidgeRegression.png")

#\[T]/
