import numpy as np
import pandas as pd
from numpy import mean
import os
import math
import matplotlib.pyplot as plt
"""#reading the updated file with bmi column filled with mean
df=pd.read_csv("C:\\Users\\neha_\\OneDrive\\Desktop\\py progs\\healthcare-dataset-stroke-data-updated.csv")
print(df)
df["age"] = df["age"].round()
print(df["age"])
#updating csv file
old="C:\\Users\\neha_\\OneDrive\\Desktop\\py progs\\healthcare-dataset-stroke-data-updated.csv"
new="C:\\Users\\neha_\\OneDrive\\Desktop\\py progs\\healthcare-dataset-stroke-data-update2.csv"
df.to_csv(new, index=False)
os.remove(old)
"""#reading new csv file with age column being rounded off
d=pd.read_csv("C:\\Users\\neha_\\OneDrive\\Desktop\\py progs\\healthcare-dataset-stroke-data-update2.csv")
print(d)












"""#checking whether bmi of a person can make a person prone to heart diseases
x1 = d['bmi']
y = d['heart_disease']
# Calculate the slope (m) and y-intercept (c)
m, c = np.polyfit(x1, y, 1)
# Generate the regression line
regression_line = m * x1 + c
# Create the scatter plot of the data points
plt.scatter(x1, y, color='b', label='Data Points')
plt.plot(x1, regression_line, color='r', label='Regression Line')
plt.xlabel('BMI')
plt.ylabel('Heart Disease')
plt.legend()
plt.show()

#checking whether hypertension  can make a person prone to heart diseases
x2=d['hypertension']
y=d['heart_disease']
m,c=np.polyfit(x2,y,1)
reg_line=m*x2+c
plt.scatter(x2,y,color='b',label='data')
plt.plot(x2,reg_line,color='r',label='regression line')
plt.xlabel("hypertension")
plt.ylabel("heart disease")
plt.legend()
plt.show()

#checking whether stroke can make a person prone to heart diseases 
x3=d['stroke']
y=d['heart_disease']
m,c=np.polyfit(x3,y,1)
reg_line=m*x3+c
plt.scatter(x3,y,color='b',label='data')
plt.plot(x3,reg_line,color='r',label='regression line')
plt.xlabel("stroke")
plt.ylabel("heart disease")
plt.legend()
plt.show()

##checking whether average glucose level of a person can make a person prone to heart diseases
x4=d['avg_glucose_level']
y=d['heart_disease']
m,c=np.polyfit(x4,y,1)
reg_line=m*x4+c
plt.scatter(x4,y,color='b',label='data')
plt.plot(x4,reg_line,color='r',label='regression line')
plt.xlabel("avg glucose level")
plt.ylabel("heart disease")
plt.legend()
plt.show()
"""
