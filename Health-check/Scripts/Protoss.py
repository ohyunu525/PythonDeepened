import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

def clearPlt():
    plt.clf()
    plt.cla()
def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            print("Error: \"", directory, "\" already exists.", sep="")
    except OSError:
        print("Error: Can't make \"", directory, "\".", sep="")

#ProjectSetting
if os.name == "posix":
    plt.rc("font", family="AppleGothic")
else:
    plt.rc("font", family="Malgun Gothic")

plt.rc("axes", unicode_minus=False)



df = pd.read_csv("../Sources/NHIS_OPEN_GJ_2017_v1.1.csv", encoding="CP949")

createDirectory("../Outputs/CategoricalData")

df_sample = df.sample(1000, random_state=1)

df["음주여부"].value_counts().plot.bar()
plt.savefig("../Outputs/CategoricalData/CategoricalData_1")

sns.countplot(x="음주여부", data=df)
plt.savefig("../Outputs/CategoricalData/CategoricalData_2")

sns.countplot(x="음주여부", data=df, hue="성별코드")
plt.savefig("../Outputs/CategoricalData/CategoricalData_3")

sns.set(font_scale=1.5, font="Malgun Gothic")
sns.countplot(x="음주여부", data=df, hue="성별코드")
plt.savefig("../Outputs/CategoricalData/CategoricalData_4")

sns.countplot(data=df, x="연령대코드(5세단위)")
plt.savefig("../Outputs/CategoricalData/CategoricalData_5")

sns.countplot(data=df, x="연령대코드(5세단위)", hue="음주여부")
plt.savefig("../Outputs/CategoricalData/CategoricalData_6")

plt.figure(figsize=(15, 4))
sns.countplot(data=df, x="신장(5Cm단위)")
plt.savefig("../Outputs/CategoricalData/CategoricalData_7")

plt.figure(figsize=(15, 4))
sns.countplot(data=df, x="체중(5Kg단위)")
plt.savefig("../Outputs/CategoricalData/CategoricalData_8")

plt.figure(figsize=(15, 4))
sns.countplot(data=df, x="신장(5Cm단위)", hue="성별코드")
plt.savefig("../Outputs/CategoricalData/CategoricalData_9")

plt.figure(figsize=(15, 4))
sns.countplot(data=df, x="체중(5Kg단위)", hue="성별코드")
plt.savefig("../Outputs/CategoricalData/CategoricalData_10")

sns.barplot(data=df, x="연령대코드(5세단위)", y="총콜레스테롤")
plt.savefig("../Outputs/CategoricalData/CategoricalData_11")

sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="총콜레스테롤")
plt.savefig("../Outputs/CategoricalData/CategoricalData_12")

sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="총콜레스테롤", hue="음주여부")
plt.savefig("../Outputs/CategoricalData/CategoricalData_13")

plt.figure(figsize=(12, 4))
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="총콜레스테롤", hue="흡연상태")
plt.savefig("../Outputs/CategoricalData/CategoricalData_14")

plt.figure(figsize=(12, 4))
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="트리글리세라이드", hue="음주여부")
plt.savefig("../Outputs/CategoricalData/CategoricalData_15")

plt.figure(figsize=(12, 4))
sns.barplot(data=df, x="연령대코드(5세단위)", y="트리글리세라이드", hue="음주여부", ci=95)
plt.savefig("../Outputs/CategoricalData/CategoricalData_16")

plt.figure(figsize=(12, 4))
sns.barplot(data=df, x="연령대코드(5세단위)", y="트리글리세라이드", hue="음주여부", ci="sd")
plt.savefig("../Outputs/CategoricalData/CategoricalData_17")

plt.figure(figsize=(12, 4))
sns.barplot(data=df, x="연령대코드(5세단위)", y="체중(5Kg단위)", hue="성별코드", ci=None)
plt.savefig("../Outputs/CategoricalData/CategoricalData_18")
#\[T]/