# -*- coding: utf-8 -*-
"""Masterclass_lesson_script.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kEFUeqrLMe4idj5GkqI7weOqXHlilIuW
"""

# Importing Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the data inside a pandad DataFrame we named df
df = pd.read_csv("***.csv")

# DataFrame information
df.***()

# To select columns in pandas of a dataframe format:
# DataFrameName["Selected Column"]
# Example only selecting "t_min" column:
df[***]

# To select a column in a method
# DataFrameName.MethodName(["Selected Column"])
# Example Dropping columns we do not need using .drop() method:
# axis = 1 makes sure we drop a column not a row
# inplace = True makes sure we replace the original df with the new df with the dropped column
df.drop([***], axis=1, inplace=True)

# First 20 rows of DataFrame (Default is 5)
df.head(***)

# Descriptives temp_transport column of DataFrame by selecting it and using 
# .describe() method
df[***].describe()

# Write the answer here: "Time left when the cooler breaks at 0 degrees: ... min"
# Use .query() method and write down the query we need. Afterwords select the
# correct column and use .iloc[0] to select the 1st value.
cooler_alert_first_time = (df
                           .query("*** == ***")["***"]
                           .iloc[0])
product_alert_first_time = (df
                            .query("*** == ***")["***"]
                            .iloc[0])
print("Time left when the cooler breaks at 0 degrees: {} min".format(***))

# Example scatter plot in Matplotlib
df.plot(kind='scatter',x='t_min', y='temp_transport')

# Scatter plot in Seaborn 
plt.figure(figsize=(10,7))
sns.scatterplot(data=***, x=***, y=***)

plt.hlines(-17, xmin=***, xmax=2000, colors='g')
plt.hlines(-2, xmin=***, xmax=2000, colors='r')

# Adding these to the top packages:
# Please copy them and paste them in the 1st Cell of this notebook
# After pasting them run the 1st cell again to load the packages
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures  
from sklearn.metrics import mean_squared_error

# reshape the data for input and output model.
x = (df[***]
     .to_numpy()
     .reshape(-1, 1)
     )
y = (df[***]
     .to_numpy()
     .reshape(-1, 1)
     )

# Innitiate a Linear Regression and fit it ove our model
# make a prediction with only using the time variable
model_linear = LinearRegression()
model_linear.fit(x, y)
y_linear_pred = model_linear.predict(x)

# Create a simple scatter plot (s=1 gives a smaller dot in the plot)
# Also create a plot of the prediction that our model made
plt.scatter(x, y, s=1)
plt.plot(x, y_linear_pred, color='m')
plt.show()

# Create polynomial features for a Polynomial Regression
# Transform the x into x_poly
polynomial_features = PolynomialFeatures(degree=***)
x_poly = polynomial_features.fit_transform(x)

# Initiate a new LinearRegression but now fit it with x_poly
# Make a prediction with this new model
model_poly = ***()
model_poly.fit(***, y)
y_poly_pred = ***.***(***)

# Create a simple scatter plot of the new model
# Also create a plot of the prediction that our model made
plt.scatter(***, ***, s=1)
plt.plot(***, ***, color='m')
plt.***()

# Find the index where the product_alert would go off and print the time
max_time_idx = min(np.where(*** > ***)[0])
time_prod_alert = x[max_time_idx][0]
print(time_prod_alert)

# Find the index where the cooler_alert would go off and print the time
start_time_idx = max(np.where(*** <= ***)[0])
time_cooler_alert = x[start_time_idx][0]
print(time_cooler_alert)

# Print out the time left 
print("Time left: {} min".format(*** - ***))

# Example function:
def function_name(variable_1,variable_2):

  """
  This function adds variable_1 and variable_2 together

  Parameters:
    Numeric numbers variable_1 and variable_2

  Returns:
    variable_1 added to variable_2
  """
  # create the function while using the variables 
  output = variable_1 + variable_2

  # use a return statement to output the function
  # in this case we print an equasion
  # the return statement also closes the function
  return print("{} + {} = {}".format(variable_1,variable_2,output))

# After creating the function we can use it like this:
function_name(5,3)

# Create a function to do all these previous steps for all outside temp datasets
def calculate_time_left(datasets):
  """
  This function creates a dictionary of descrete predicted outcomes of how long 
  it takes a truck cooler to heat up before products go bad on 7 different 
  outside temperature datasets: 0, 5, 10, 15, 20, 25, 30 degrees.
  This dictionary could be used to predict continuous values of outside
  temperatures for the IoT device.

  Parameters:
    Temperature Datasets: 0, 5, 10, 15, 20, 25, 30 degrees. 
    With the columns: temp_outside, t_min, temp_transport

  Returns:
    Dictionary of discrete predicted outcomes of our model in time for different degrees.
  """
  times_left = {}
  for dataset in datasets:
      df = pd.read_csv(dataset)
      outside_temp = df[***][0]

      # Reshape model
      # Polynomial features
      # Linear regression
      # Prediction

      max_time_idx = min(np.where(*** > ***)[0])
      start_time_idx = max(np.where(*** <= ***)[0])
      times_left[outside_temp] = (x[max_time_idx] - x[start_time_idx])[0]
  return times_left

# Load all the dataset names into a list
temps = np.linspace(0,30,7,dtype=int)
datasets = ["test_model_"+str(x)+".csv" for x in temps]
# Use the new function to create the dictionary
cal_time_left = calculate_time_left(datasets)

# Create the new DataFrame for the final model
final_df = pd.DataFrame(list(cal_time_left.items()),
                        columns = ["temp_outside","time_left"]
                        ) 
final_df

# Reshape new data for model
***

# Initiate model and predict using Linear regression
***

# Plot predictions in a scatter plot with the linear prediction
***

# Initiate model with polynomial features
***

# Plot the predictions of the polynomial features model
***

# Compare MSE
mse_linear = mean_squared_error(y, ***)
mse_poly = mean_squared_error(y, ***)

print("MSE of linear model:\t {} \nMSE of polynomial model: {}"
      .format(mse_linear, 
              mse_poly
              )
      )

# Compare R-Squared
r2_linear = model_linear.score(x, y)
r2_poly = model_poly.score(***, y)

print("Rsquared of linear model: \t{}\nRsquared of polynomial model:\t{}"
      .format(r2_linear, 
              r2_poly
              )
      )
