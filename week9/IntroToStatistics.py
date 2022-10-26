#as we did in (analyze data) section, we use the same code to get more information
print (full_health_data.describe())

#Task: Find the 10% percentile for Max_Pulse
import numpy as np

Max_Pulse= full_health_data["Max_Pulse"]
percentile10 = np.percentile(Max_Pulse, 10)
print(percentile10)

#StandartDeviation(std)
#we need this to know how much observations are spread out (measure of uncertainty)
'''
A low standard deviation means that most of the numbers are close to the mean (average) value.
A high standard deviation means that the values are spread out over a wider range.
'''
#What does these numbers mean?
#The data shown from code give us standart deviation of all measurments
import numpy as np

std = np.std(full_health_data)
print(std)

#CoefficientOfVariation
#Shows how large σ is

import numpy as np

cv = np.std(full_health_data) / np.mean(full_health_data)
print(cv)


#StatisticsVariance

#variance also can tell  us about how much data is spread out
#simply it is the std*std or σ^2

#to calculate variance we need 4 difficult calculations, but in python we run code:
import numpy as np

var = np.var(health_data)
print(var)

#to calc variance of full data set we run:
import numpy as np

var_full = np.var(full_health_data)
print(var_full)

