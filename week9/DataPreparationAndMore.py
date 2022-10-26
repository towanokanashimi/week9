import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")
print(health_data)
#if file is large we can use print(health_data.head()) instead
#I dont know where to find given table, so I will just copy the code and read more diligently

#DataCleaning

#we can use this code for file in (DataPreparation) to remove rows with Nans in it
health_data.dropna(axis=0,inplace=True)
print(health_data)

#DataCategories

#also for this file, if we want  to know what data types are used, we will use:
print(health_data.info())
#we can see that there are 2 different types of data, so in that way we can use code below to make all data types 'float64'
health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)
print (health_data.info())

#AnalyzeData

#for basic analytics we can use code below to know count, mean, std, min, different percentage and max:
print(health_data.describe())