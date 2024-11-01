
#%%
import numpy as np
import pandas as pd
apples = pd.read_csv('/Users/alexa/Documents/git py analysis/Apple Stocks/02-data/AppleStockPrices.csv')
print(apples)
#%%
# Producing the descriptive statistics

## Count
values_count = apples['Open'].count()  # Count Open


## Mean ------------------------------------------------------------------------------------------------

## Mean, per column variables
mean_open = apples['Open'].mean() # Mean Open
mean_high = apples['High'].mean() # Mean High
mean_low = apples['Low'].mean() # Mean Low
mean_close = apples['Close'].mean() # Mean Close
mean_volume = apples['Volume'].mean()

## Mean dictionary for mean
mean_values = {
    "Mean Open": apples['Open'].mean(), # Mean Open
    "Mean High": apples['High'].mean(), # Mean High
    "Mean Low": apples['Low'].mean(), # Mean Low
    "Mean Close": apples['Close'].mean(), # Mean Close
}

## Median ------------------------------------------------------------------------------------------------

### Per-column variables median
median_open = apples['Open'].median() # Max Open
median_high = apples['High'].median() # Max High
median_low = apples['Low'].median() # Max Low
median_close = apples['Close'].median() # Max Close
median_volume = apples['Volume'].median() # Max Volume

### Dictionary median
median_values = {
    "Median Open": apples['Open'].median(), # Median Open
    "Median High": apples['High'].median(), # Median High
    "Median Low": apples['Low'].median(), # Median Low
    "Median Close": apples['Close'].median(), # Median Close
}

## max, min and range ------------------------------------------------------------------------------------------------

### Per-column variables max, min, range

#### Max
max_open = apples['Open'].max() # Max Open
max_high = apples['High'].max() # Max High
max_low = apples['Low'].max() # Max Low
max_close = apples['Close'].max() # Max Close
max_volume = apples['Volume'].max() # Max Volume

#### Min
min_open = apples['Open'].min() # Min Open
min_high = apples['High'].min() # Min High
min_low = apples['Low'].min() # Min Low
min_close = apples['Close'].min() # Min Close
min_volume = apples['Volume'].min() # Min Volume

#### Range
range_open = abs(max_open - min_open) # Range Open
range_high = abs(max_high - min_high) # Range High
range_low = abs(max_low - min_low) # Range Low
range_close = abs(max_close - min_close) # Range Close
range_volume = abs(max_volume - min_volume) # Range Volume

### Dictionary Max, Min, Range
range_max_min = {
    "Max Open": apples['Open'].max(), # Max Open
    "Min Open": apples['Open'].min(), # Min Open
    "Range Open": range_open, # Range Open
    "Max High": apples['High'].max(), # Max High
    "Min High": apples['High'].min(), # Min High
    "Range High": range_high, # Range High
    "Max Low": apples['Low'].max(), # Max Low
    "Min Low": apples['Low'].min(), # Min Low
    "Range Low": range_low, # Range Low
    "Max Close": apples['Close'].max(), # Max Close
    "Min Close": apples['Close'].min(), # Min Close
    "Range Close": range_close # Range Close
}

## Variance ------------------------------------------------------------------------------------------------

## Variance ind. columns
var_open = apples['Open'].var() # var Open
var_high = apples['High'].var() # var High
var_low = apples['Low'].var() # var Low
var_close = apples['Close'].var() # var Close
var_volume = apples['Volume'].var() # var Volume

## Variance dict.
var_dict = {
    "Variance Open": apples['Open'].var(), # var Open
    "Variance High": apples['High'].var(), # var High
    "Variance Low": apples['Low'].var(), # var Low
    "SVariance Close": apples['Close'].var(), # var Close
}

## Standard Deviation ------------------------------------------------------------------------------------------------

### std.dev ind. columns
std_open = apples['Open'].std() # Std Open
std_high = apples['High'].std() # Std High
std_low = apples['Low'].std() # Std Low
std_close = apples['Close'].std() # Std Close
std_volume = apples['Volume'].std() # Std Volume

### Std. Dict. 
std_dev_dict = {
    "Std.Dev Open": apples['Open'].std(), # Std Open
    "Std.Dev High": apples['High'].std(), # Std High
    "Std.Dev Low": apples['Low'].std(), # Std Low
    "Std.Dev Close": apples['Close'].std(), # Std Close
}

# Divider ------------------------------------------------------------------------------------------------

#%%
# Printing

## Print count
print("Count: ", values_count)

### Print a seperator 
print("--------------------")

## Print Mean
for key, value in mean_values.items():
    print(f"{key}: {value:.2f}")

### Print a seperator 
print("--------------------")

## Print Median
for key, value in median_values.items():
    print(f"{key}: {value:.2f}")

### Print a seperator 
print("--------------------")

## Print max, min, range
for key, value in range_max_min.items():
    print(f"{key}: {value:.2f}")

### Print a seperator 
print("--------------------")


## Print Variance
for key, value in var_dict.items():
    print(f"{key}: {value:.2f}")

### Print a seperator 
print("--------------------")

## Print Standard Deviation
for key, value in std_dev_dict.items():
    print(f"{key}: {value:.2f}")

### Print a seperator 
print("--------------------")

# Divider ------------------------------------------------------------------------------------------------
#%%
# Mean Array
mean_array = x_1 = np.array([format(mean_open, ".2f"), format(mean_high, ".2f"), format(mean_low, ".2f"), format(mean_close, ".2f")]) #define array
x_1 = mean_array.reshape((-1, 1)) # Transpose array

print('Mean array')
print(x_1)
#%%
# Median array
median_array = x_2 = np.array([format(median_open, ".2f"), format(median_high, ".2f"), format(median_low, ".2f"), format(median_close, ".2f")]) #define array
x_2 = median_array.reshape((-1, 1)) # Transpose array

print('Median array')
print(x_2)
#%%
# Max array
max_array = x_3 = np.array([format(max_open, ".2f"), format(max_high, ".2f"), format(max_low, ".2f"), format(max_close, ".2f")]) #define array
x_3 = max_array.reshape((-1, 1)) # Transpose array

print('Max array')
print(x_3)
#%%
# Min array
min_array = x_4 = np.array([format(min_open, ".2f"), format(min_high, ".2f"), format(min_low, ".2f"), format(min_close, ".2f")]) #define array
x_4 = min_array.reshape((-1, 1)) # Transpose array

print('Min array')
print(x_4)
#%%
# Range array
range_array = x_5 = np.array([format(range_open, ".2f"), format(range_high, ".2f"), format(range_low, ".2f"), format(range_close, ".2f")]) #define array
x_5 = range_array.reshape((-1, 1)) # Transpose array

print('Range array')
print(x_5)
#%%
# Variance array
var_array = x_6 = np.array([format(var_open, ".2f"), format(var_high, ".2f"), format(var_low, ".2f"), format(var_close, ".2f")]) #define array
x_6 = var_array.reshape((-1, 1)) # Transpose array

print('Variance array')
print(x_6)
#%%
# Std. Dev. array
std_array = x_7 = np.array([format(std_open, ".2f"), format(std_high, ".2f"), format(std_low, ".2f"), format(std_close, ".2f")]) #define array
x_7 = std_array.reshape((-1, 1)) # Transpose array

print('Std. Dev. array')
print(x_7)
#%%
