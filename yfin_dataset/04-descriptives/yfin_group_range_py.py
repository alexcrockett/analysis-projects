#%%
# Import modules and variables we need 

import pandas as pd
yfin_csv = pd.read_csv(r'https://raw.githubusercontent.com/alexcrockett/Jupyter-Playground/personal/yfin_dataset/02-data/stock_details_5_years.csv')

#%%
# Finding the fourth quartile of data

## Compute the average between high and low for each company:
yfin_csv['Average'] = (yfin_csv['High'] + yfin_csv['Low']) / 2 # Here we are defining a new column called Average

## Group by company and compute the mean of the 'Average' column
company_averages = yfin_csv.groupby('Company')['Average'].mean() # Now we create a new variable to group companies with their means and compute means for these groups

## Find the quartiles
first_quartile = company_averages.quantile(0.25) # Define the 1st quartile
fourth_quartile = company_averages.quantile(0.75) #Define the 4th quartile

## Segment the quartiles
companies_in_first_quartile = company_averages[company_averages <= first_quartile] # Identify those in the 1st quartile
companies_in_fourth_quartile = company_averages[company_averages >= fourth_quartile] # Identify those in the 4th quartile

## Print the first quartile
print("Companies in the first quartile:")
print(companies_in_first_quartile)
print("-------------------")

print("Companies in the fourth quartile:")
print(companies_in_fourth_quartile)
print("-------------------")

# Sort the data

## Sort companies in the first quartile in ascending order to find the lowest
lowest_in_first_quartile = companies_in_first_quartile.sort_values(ascending=True)
highest_in_first_quartile = companies_in_first_quartile.sort_values(ascending=False)

## Sort companies in the fourth quartile in descending order to find the highest
lowest_in_fourth_quartile = companies_in_fourth_quartile.sort_values(ascending=True)
highest_in_fourth_quartile = companies_in_fourth_quartile.sort_values(ascending=False)

## Print the lowest company in the first quartile
print("Lowest company in the first quartile:")
print(lowest_in_first_quartile.head(1))  # .head(1) gets the top company after sorting in ascending order
print("-------------------")

## Print the highest company in the first quartile
print("Highest in the first quartile")
print(highest_in_first_quartile.head(1))
print("-------------------")

## Print the lowest company in the fourth quartile
print("Lowest company in the fourth quartile:")
print(lowest_in_fourth_quartile.head(1))  # .head(1) gets the top company
print("-------------------")


# Print the highest company in the fourth quartile
print("Highest company in the fourth quartile:")
print(highest_in_fourth_quartile.head(1))  # .head(1) gets the top company
print("-------------------")

#%%
# Range statistics

## Defining the range values
yfin_csv['Range'] = yfin_csv['High'] - yfin_csv['Low'] # Subtracting Low from High to get the actual range

## Grouping companies by their range and calculating statistics
company_ranges_mean = yfin_csv.groupby('Company')['Range'].mean()
company_ranges_min = yfin_csv.groupby('Company')['Range'].min()
company_ranges_max = yfin_csv.groupby('Company')['Range'].max()
company_ranges_std = yfin_csv.groupby('Company')['Range'].std()

## Sorting by the standard deviation of the range scores

### Mean
highest_mean_range = company_ranges_mean.sort_values(ascending=False)
lowest_mean_range = company_ranges_mean.sort_values(ascending=True)

### Min
highest_min_range = company_ranges_min.sort_values(ascending=False)
lowest_min_range = company_ranges_min.sort_values(ascending=True)

### Max
highest_max_range = company_ranges_max.sort_values(ascending=False)
lowest_max_range = company_ranges_max.sort_values(ascending=True)

### Std
highest_std_range = company_ranges_std.sort_values(ascending=False)
lowest_std_range = company_ranges_std.sort_values(ascending=True)

## Printing

### Mean scores
print("Mean Range")
print(company_ranges_mean)
print("-------------------")

### Min scores
print("Min Range")
print(company_ranges_min)
print("-------------------")

### Max scores
print("Max Range")
print(company_ranges_max)
print("-------------------")

### Standard deviation scores
print("Standard Deviation of Range")
print(company_ranges_std)
print("-------------------")

print("-------------------")
print("-------------------")

### Highest/lowest mean
print("Company with Highest Mean Range")
print(highest_mean_range.head(1))
print("-------------------")

print("Company with Lowest Mean Range")
print(lowest_mean_range.head(1))
print("-------------------")

### Highest/lowest Min
print("Company with Highest Min Range")
print(highest_min_range.head(1))
print("-------------------")

print("Company with Lowest Min Range")
print(lowest_min_range.head(1))
print("-------------------")

### Highest/lowest Max
print("Company with Highest Max Range")
print(highest_max_range.head(1))
print("-------------------")

print("Company with Lowest Max Range")
print(lowest_max_range.head(1))
print("-------------------")

### Highest/lowest Std
print("Company with Highest Std Range")
print(highest_std_range.head(1))
print("-------------------")

print("Company with Lowest Std Range")
print(lowest_std_range.head(1))
print("-------------------")

#%%
### Highest/lowest Max
print("Company with Highest Max Range")
print(highest_max_range.head(20))
print("-------------------")

print("Company with Lowest Min Range")
print(lowest_min_range.head(20))
print("-------------------")
#%%
