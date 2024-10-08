#%%
# import libraries and data

## Libraries
import numpy as np
import pandas as pd

## Data
yfin_csv = pd.read_csv(r'https://raw.githubusercontent.com/alexcrockett/Jupyter-Playground/personal/yfin_dataset/02-data/stock_details_5_years.csv')

### Becuase there is a lot of data we will just print the first 5 rows
print(yfin_csv.head(5))
#%%
# Computing the descriptive statistics

## Count ------------------------------------------------------------------------------------------------
count_open = yfin_csv['Open'].count() # Count Open

## Mean ------------------------------------------------------------------------------------------------

### Per Columns
mean_open = yfin_csv['Open'].mean() # Mean Open
mean_high = yfin_csv['High'].mean() # Mean High
mean_low = yfin_csv['Low'].mean() # Mean Low
mean_close = yfin_csv['Close'].mean() # Mean Close
mean_volume = yfin_csv['Volume'].mean() # Mean Volume
mean_div = yfin_csv['Dividends'].mean() # Mean Dividends

### Dict.
di_mean1 = {
    "mean open": yfin_csv['Open'].mean(),
    "mean high": yfin_csv['High'].mean(),
    "mean low": yfin_csv['Low'].mean(),
    "mean close": yfin_csv['Close'].mean(),
    "mean volume": yfin_csv['Volume'].mean(),
    "mean dividends": yfin_csv['Dividends'].mean(),
}

## Median ------------------------------------------------------------------------------------------------

### Per Columns
median_open = yfin_csv['Open'].median() # median Open
median_high = yfin_csv['High'].median() # median High
median_low = yfin_csv['Low'].median() # median Low
median_close = yfin_csv['Close'].median() # median Close
median_volume = yfin_csv['Volume'].median() # median Volume
median_div = yfin_csv['Dividends'].median() # median Dividends

### Dict.
di_median1 = {
    "median open": yfin_csv['Open'].median(),
    "median high": yfin_csv['High'].median(),
    "median low": yfin_csv['Low'].median(),
    "median close": yfin_csv['Close'].median(),
    "median volume": yfin_csv['Volume'].median(),
    "median dividends": yfin_csv['Dividends'].median(),
}

## Min, Max, Range ------------------------------------------------------------------------------------------------

### Per Columns

#### max
max_open = yfin_csv['Open'].max() # max Open
max_high = yfin_csv['High'].max() # max High
max_low = yfin_csv['Low'].max() # max Low
max_close = yfin_csv['Close'].max() # max Close
max_volume = yfin_csv['Volume'].max() # max Volume
max_div = yfin_csv['Dividends'].max() # max Dividends

#### min
min_open = yfin_csv['Open'].min() # min Open
min_high = yfin_csv['High'].min() # min High
min_low = yfin_csv['Low'].min() # min Low
min_close = yfin_csv['Close'].min() # min Close
min_volume = yfin_csv['Volume'].min() # min Volume
min_div = yfin_csv['Dividends'].min() # min Dividends

#### range
range_open = abs(max_open - min_open) # range Open
range_high = abs(max_high - min_high) # range High
range_low = abs(max_low - min_low) # range Low
range_close = abs(max_close - min_close) # range Close
range_volume = abs(max_volume - min_volume) # range Volume
range_div = abs(max_div - min_div) # range Dividends

### Dict.

di_max_min_range = {
    "min open": yfin_csv['Open'].min(),
    "max open": yfin_csv['Open'].max(),
    "range open": range_open,
    "min high": yfin_csv['High'].min(),
    "max high": yfin_csv['High'].max(),
    "range high": range_high,
    "min low": yfin_csv['Low'].min(),
    "max low": yfin_csv['Low'].max(),
    "range low": range_low,
    "min close": yfin_csv['Close'].min(),
    "max close": yfin_csv['Close'].max(),
    "range close": range_close,
    "min volume": yfin_csv['Volume'].min(),
    "max volume": yfin_csv['Volume'].max(),
    "range volume": range_volume,
    "min dividends": yfin_csv['Dividends'].min(),
    "max dividends": yfin_csv['Dividends'].max(),
    "range dividends": range_div,
}

## Variance ------------------------------------------------------------------------------------------------

### Per Columns
var_open = yfin_csv['Open'].var() # var Open
var_high = yfin_csv['High'].var() # var High
var_low = yfin_csv['Low'].var() # var Low
var_close = yfin_csv['Close'].var() # var Close
var_volume = yfin_csv['Volume'].var() # var Volume
var_div = yfin_csv['Dividends'].var() # var Dividends

### Dict.
di_var1 = {
    "var open": yfin_csv['Open'].var(),
    "var high": yfin_csv['High'].var(),
    "var low": yfin_csv['Low'].var(),
    "var close": yfin_csv['Close'].var(),
    "var volume": yfin_csv['Volume'].var(),
    "var dividends": yfin_csv['Dividends'].var(),
}

## Standard Deviation ------------------------------------------------------------------------------------------------
### Per column
std_open = yfin_csv['Open'].std() # std Open
std_high = yfin_csv['High'].std() # std High
std_low = yfin_csv['Low'].std() # std Low
std_close = yfin_csv['Close'].std() # std Close
std_volume = yfin_csv['Volume'].std() # std Volume
std_div = yfin_csv['Dividends'].std() # std Dividends

### Dict.
di_std1 = {
    "std open": yfin_csv['Open'].std(),
    "std high": yfin_csv['High'].std(),
    "std low": yfin_csv['Low'].std(),
    "std close": yfin_csv['Close'].std(),
    "std volume": yfin_csv['Volume'].std(),
    "std dividends": yfin_csv['Dividends'].std(),
}

# Divider ------------------------------------------------------------------------------------------------
#%%
# Creating vectors for the standard descriptive statistics

## Mean
mean_array = x_1 = np.array([float(format(mean_open, ".2f")), float(format(mean_high, ".2f")), float(format(mean_low, ".2f")), float(format(mean_close, ".2f"))]) #define array
x_1 = mean_array.reshape((-1, 1)) # Transpose array


## Median
median_array = x_2 = np.array([float(format(median_open, ".2f")), float(format(median_high, ".2f")), float(format(median_low, ".2f")), float(format(median_close, ".2f"))]) #define array
x_2 = median_array.reshape((-1, 1)) # Transpose array


## Min
min_array = x_3 = np.array([float(format(min_open, ".2f")), float(format(min_high, ".2f")), float(format(min_low, ".2f")), float(format(min_close, ".2f"))]) #define array
x_3 = min_array.reshape((-1, 1)) # Transpose array


## Max
max_array = x_4 = np.array([float(format(max_open, ".2f")), float(format(max_high, ".2f")), float(format(max_low, ".2f")), float(format(max_close, ".2f"))]) #define array
x_4 = max_array.reshape((-1, 1)) # Transpose array


## Range
range_array = x_5 = np.array([float(format(range_open, ".2f")), float(format(range_high, ".2f")), float(format(range_low, ".2f")), float(format(range_close, ".2f"))]) #define array
x_5 = max_array.reshape((-1, 1)) # Transpose array


## Variance
var_array = x_6 = np.array([float(format(var_open, ".2f")), float(format(var_high, ".2f")), float(format(var_low, ".2f")), float(format(var_close, ".2f"))]) #define array
x_6 = var_array.reshape((-1, 1)) # Transpose array


## Standard deviation
std_array = x_7 = np.array([float(format(std_open, ".2f")), float(format(std_high, ".2f")), float(format(std_low, ".2f")), float(format(std_close, ".2f"))]) #define array
x_7 = std_array.reshape((-1, 1)) # Transpose array

#%%
