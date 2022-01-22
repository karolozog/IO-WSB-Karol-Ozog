from mlxtend.plotting import plot_decision_regions
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import warnings
warnings.filterwarnings('ignore')

diabetes_data = pd.read_csv("diabetes.csv")

diabetes_data_copy = diabetes_data.copy(deep = True)
diabetes_data_copy[["glucose-concentr", "blood-pressure", "skin-thickness", "insulin", "mass-index"]] = diabetes_data_copy[["glucose-concentr", "blood-pressure", "skin-thickness", "insulin", "mass-index"]].replace(0,np.NaN)

print(diabetes_data_copy.isnull().sum())

p = diabetes_data.hist(figsize = (23,15))

diabetes_data_copy['glucose-concentr'].fillna(diabetes_data_copy['glucose-concentr'].mean(), inplace = True)
diabetes_data_copy['blood-pressure'].fillna(diabetes_data_copy['blood-pressure'].mean(), inplace = True)
diabetes_data_copy['skin-thickness'].fillna(diabetes_data_copy['skin-thickness'].median(), inplace = True)
diabetes_data_copy['insulin'].fillna(diabetes_data_copy['insulin'].median(), inplace = True)
diabetes_data_copy['mass-index'].fillna(diabetes_data_copy['mass-index'].median(), inplace = True)


x = np.arange(5)
value = [5,35, 227, 374, 11]

fig, ax = plt.subplots()
plt.bar(x, value)
plt.xticks(x, ("glucose-concentr", "blood-pressure", "skin-thickness", "insulin", "mass-index"))
plt.show()