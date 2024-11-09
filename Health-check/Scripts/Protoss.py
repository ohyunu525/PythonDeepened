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

createDirectory("../Outputs/EntireDatas")

h1 = df.hist(figsize=(15, 15))
plt.savefig("../Outputs/EntireDatas/EntireDatas_1")
clearPlt()

h2 = df.iloc[:, :12].hist(figsize=(15,15))
plt.savefig("../Outputs/EntireDatas/EntireDatas_2")
clearPlt()

h3 = df.iloc[ :, 12:24].hist(figsize=(15,15), bins=100)
plt.savefig("../Outputs/EntireDatas/EntireDatas_3")
clearPlt()

h4 = df.iloc[ :, 24:].hist(figsize=(15,15), bins=100)
plt.savefig("../Outputs/EntireDatas/EntireDatas_4")
clearPlt()

h5 = df.iloc[ :, 24:].hist(figsize=(15,15), bins=10)
plt.savefig("../Outputs/EntireDatas/EntireDatas_5")

#\[T]/