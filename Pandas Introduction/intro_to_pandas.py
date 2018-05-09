import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print(pd.__version__)

# Creating a Series

city_names = pd.Series(['Xerem', 'Imbarie', 'Piabeta'])
print(city_names)

population = pd.Series([123123,4325225,6345212])

# Creating Data Frame

''' DataFrame objects can be created by passing a dict 
mapping string column names to their respective Series. 
If the Series don't match in length, missing values are 
filled with special NA/NaN values '''

df = pd.DataFrame({'City Name' : city_names, 'Population' : population})
print(df)


''' But most of the time, you load an entire file into a DataFrame. 
The following example loads a file with California housing data. '''

california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
print(california_housing_dataframe.describe())
print(california_housing_dataframe)
print(california_housing_dataframe.head())
#print(type(california_housing_dataframe.hist('housing_median_age')))
#print(california_housing_dataframe.hist('housing_median_age'))
#california_housing_dataframe.hist('housing_median_age')
#plt.plot(california_housing_dataframe.hist('housing_median_age'))


#Acessing Data

print(type(df['City Name']))
print(df['City Name'])

print(type(df['City Name'][1]))
print(df['City Name'][1])

#Manipulating Data

population = population / 1000

log = np.log(population)
print(log)

# The example below creates a new Series that indicates whether population is over one million

print(population.apply(lambda val: val > 1000000))
df['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
df['Population density'] = df['Population'] / df['Area square miles']
print(df)