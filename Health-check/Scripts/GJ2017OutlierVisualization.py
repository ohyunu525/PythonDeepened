import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

#ProjectSetting
if os.name == "posix":
    plt.rc("font", family="AppleGothic")
else:
    plt.rc("font", family="Malgun Gothic")

plt.rc("axes", unicode_minus=False)

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


df = pd.read_csv("../Sources/NHIS_OPEN_GJ_2017_v1.1.csv", encoding="CP949")

createDirectory("../Outputs/GJ2017Outlier")

df.isnull().sum().plot(figsize=(10, 9))
plt.savefig("../Outputs/GJ2017Outlier/GJ2017Outlier_1")

clearPlt()

df.isnull().sum().plot.bar(figsize=(10, 9))
plt.savefig("../Outputs/GJ2017Outlier/GJ2017Outlier_2")

clearPlt()

df.isnull().sum().plot.barh(figsize=(10, 9))
plt.savefig("../Outputs/GJ2017Outlier/GJ2017Outlier_3")

#\[T]/