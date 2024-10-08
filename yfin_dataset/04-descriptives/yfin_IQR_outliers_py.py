#!/usr/bin/env python
# coding: utf-8

# Importing libraries and variables

import pandas as pd
yfin_csv = pd.read_csv(r'https://raw.githubusercontent.com/alexcrockett/Jupyter-Playground/personal/yfin_dataset/02-data/stock_details_5_years.csv')
from yfin_group_range_py import company_averages, first_quartile, fourth_quartile

## Define the 3rd Quartile and median
median = company_averages.quantile(0.5)  # The median (50th percentile)
third_quartile = fourth_quartile  # The third quartile (75th percentile)

## Define companies in the third quartile
companies_in_third_quartile = company_averages[(company_averages > median) & (company_averages <= third_quartile)]

# Define the IQR
IQR = third_quartile - first_quartile

print("IQR= ", float(str(IQR)))


# Finding outliers
outlier_scope = 1.5 * IQR 

## Calculate the lower bound for outliers
outlier_lower_bound = first_quartile - outlier_scope

## Identify outliers below the lower bound
outliers_lower = company_averages[company_averages < outlier_lower_bound]

# -----

## Calculate the upper bound for outliers
outlier_upper_bound = third_quartile + outlier_scope

## Identify outliers below the lower bound
outliers_upper = company_averages[company_averages > outlier_upper_bound]


# Review the results
print("Median: ", median)
print("--------------------")

print("IQR: ", float(str(IQR)))
print("--------------------")

print("Outliers Scope: ", outlier_scope)
print("--------------------")

print(" ") # Add a little space for reading

print("--------------------")
print("Outliers in the lower bound:")
print(outliers_lower)
print("-------------------")

print("Outliers in the upper bound:")
print(outliers_upper)
print("-------------------")

## Map companies to outliers
outlier_companies = outliers_upper.index

## Remove the comapnies
yfin_restricted_set = yfin_csv[~yfin_csv['Company'].isin(outlier_companies)]



# Revaluate the mean and median scores

## Means
mean_open_restricted = yfin_restricted_set['Open'].mean() # mean Open
mean_high_restricted = yfin_restricted_set['High'].mean() # mean High
mean_low_restricted = yfin_restricted_set['Low'].mean() # mean Low
mean_close_restricted = yfin_restricted_set['Close'].mean() # mean Close

## Medians
median_open_restricted = yfin_restricted_set['Open'].mean() # median Open
median_high_restricted = yfin_restricted_set['High'].mean() # median High
median_low_restricted = yfin_restricted_set['Low'].mean() # median Low
median_close_restricted = yfin_restricted_set['Close'].mean() # median Close

## Define a set of values to print
central_tendency_restricted = {
    "mean open": mean_open_restricted,
    "mean high": mean_high_restricted,
    "mean low": mean_low_restricted,
    "mean close": mean_close_restricted,
    "median open": median_open_restricted,
    "median high": median_high_restricted,
    "median low": median_low_restricted,
    "median close": median_close_restricted
}

# Print the results
for key, value in central_tendency_restricted.items():
    print(f"{key}: {value:.2f}")


# Finding range outliers

# Calculate the range (High - Low) for each row
yfin_csv['Range'] = yfin_csv['High'] - yfin_csv['Low']

# Calculate median and quartiles of the range
range_median = yfin_csv['Range'].median()
range_quartile_1 = yfin_csv['Range'].quantile(0.25)
range_quartile_3 = yfin_csv['Range'].quantile(0.75)

# Calculate the Interquartile Range (IQR)
range_IQR = range_quartile_3 - range_quartile_1

# Calculate the bounds for outliers
range_outlier_lower_bound = range_quartile_1 - 1.5 * range_IQR
range_outlier_upper_bound = range_quartile_3 + 1.5 * range_IQR

# Identify outliers
range_outliers_lower = yfin_csv[yfin_csv['Range'] < range_outlier_lower_bound]
range_outliers_upper = yfin_csv[yfin_csv['Range'] > range_outlier_upper_bound]

# Get the company names that are outliers
outlier_companies_lower = range_outliers_lower['Company']
outlier_companies_upper = range_outliers_upper['Company']

# Combine the lists of outlier companies
outlier_companies = pd.concat([outlier_companies_lower, outlier_companies_upper]).unique()

outlier_companies_count = outlier_companies.shape

# Remove these companies from the original DataFrame
yfin_restricted_range = yfin_csv[~yfin_csv['Company'].isin(outlier_companies)]


# Print the results
print("-------------------")
print(" ")
print("Median Range")
print(range_median)
print("-------------------")
print("Range IQR")
print(range_IQR)
print("-------------------")
print(" ")
print("-------------------")
print("Lower bound outliers")
print(outlier_companies_lower)
print("-------------------")
print("Upper bound outliers")
print(outlier_companies_upper)
print("-------------------")
print(" ")
print("-------------------")
print("outlier companies")
print(outlier_companies)

print("count: ", outlier_companies_count)

# Renaming datasets

set_1 = yfin_csv.copy() # A copy of the original data
set_2 = yfin_restricted_set.copy() # A copy of the data without outliers


