#Correlation measures relationship between variables and it's a;ways between -1 and 1

#Example of correlation = 1
import matplotlib.pyplot as plt

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='scatter')
plt.show()

#Example of correlation = -1
import matplotlib.pyplot as plt

health_data.plot(x ='Hours_Work_Before_Training', y='Calorie_Burnage', kind='scatter')
plt.show()

#Example of correlation = 0 (no correlation)
import matplotlib.pyplot as plt

health_data.plot(x ='Duration', y='Max_Pulse', kind='scatter')
plt.show()

#StatisticsCorrelationMatrix

#we can put and see all correlations in matrix form:
Corr_Matrix = round(full_health_data.corr(),2)
print(Corr_Matrix)

#Heatmap uses colors and perfect for some kid of presentations (we can use seaborn to create it)
import matplotlib.pyplot as plt
import seaborn as sns

correlation_full_health = full_health_data.corr()
axis_corr = sns.heatmap(
correlation_full_health,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(50, 500, n=500),
square=True
)
plt.show()

#CORRELATION DOES NOT IMPLY CASUALITY
#TIP: Always critically reflect over the concept of causality when doing predictions!

#LinearRegression
#The term regression is used when you try to find the relationship between variables
#Least Sqare Method - we draw dots and then draw line between them to find "average"
#Linear Regression Using One Explanatory Variable
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv("data.csv", header=0, sep=",")
x = full_health_data["Average_Pulse"]
y = full_health_data ["Calorie_Burnage"]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, slope * x + intercept)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Average_Pulse")
plt.ylabel ("Calorie_Burnage")
plt.show()

#Regration Table
#Summarized output from linear regression
'''
The content of the table includes:
• Information about the model
• Coefficients of the linear regression function
• Regression statistics
• Statistics of the coefficients from the linear regression function
• Other information that we will not cover in this module
'''
#Code to create it:
import pandas as pd
import statsmodels.formula.api as smf

full_health_data = pd.read_csv("data.csv", header=0, sep=",")
model = smf.ols('Calorie_Burnage ~ Average_Pulse', data = full_health_data)
results = model.fit()
print(results.summary())

#To perform predictions we need to use Linear Regression Function
#Example:
def Predict_Calorie_Burnage(Average_Pulse):
    return(0.3296*Average_Pulse + 346.8662)
print(Predict_Calorie_Burnage(120))
print(Predict_Calorie_Burnage(130))
print(Predict_Calorie_Burnage(150))
print(Predict_Calorie_Burnage(180))

#P - value
#The P-value is a statistical number to conclude if there is a relationship

#R - Squared
#R-Squared and Adjusted R-Squared describes how well the linear regression model fits the data points
#For visual example of R squared value we use code:
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv("data.csv", header=0, sep=",")
x = full_health_data["Duration"]
y = full_health_data ["Calorie_Burnage"]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc, x))
print(mymodel)
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Duration")
plt.ylabel ("Calorie_Burnage")
plt.show()

#Case: Use Duration + Average_Pulse to Predict Calorie_Burnage
#We need to create linear regression table:
import pandas as pd
import statsmodels.formula.api as smf

full_health_data = pd.read_csv("data.csv", header=0, sep=",")
model = smf.ols('Calorie_Burnage ~ Average_Pulse + Duration', data = full_health_data)
results = model.fit()
print(results.summary())

#How to define linear regression function?
def Predict_Calorie_Burnage(Average_Pulse, Duration):
    return(3.1695*Average_Pulse + 5.8434 * Duration - 334.5194)
print(Predict_Calorie_Burnage(110,60))
print(Predict_Calorie_Burnage(140,45))
print(Predict_Calorie_Burnage(175,20))