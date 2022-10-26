import matplotlib.pyplot as plt

from DataPreparationAndMore import health_data

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line')

plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.show()

#thanks to the lib, we can plot the graph easily and visualise data to analyse it properly
#using graph we can see direct corelation between pulse and calorie_burnage, plus to that, we can make calculations


#SlopeandIntercept

#ORDER IS VERY IMPORTANT

#Finding Intercept is not necessary for this example, but it is might be very handy foe other examples
#We need slope to ease our futher calcolations

import pandas as pd
import numpy as np

health_data = pd.read_csv("data.csv", header=0, sep=",")
x = health_data["Average_Pulse"]
y = health_data["Calorie_Burnage"]
slope_intercept = np.polyfit(x,y,1)
print(slope_intercept)

#TASK (predict calorie burnage if average pulse is 135)

#as we know slop and intercept, we also know that our funktion looks like: f(x)=2x=80
#so all we need is to paste 135 instead of x and calculate that calorie burnage will be 350

#to make this task we can use Define Math Function In Python
def my_function(x):
    return 2*x + 80
print (my_function(135))
print (my_function(140))
print (my_function(150))

#Plot a New Graph in Python
#we just added y and x max values

import matplotlib.pyplot as plt

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line'),
plt.ylim(ymin=0, ymax=400)
plt.xlim(xmin=0, xmax=150)
plt.show()