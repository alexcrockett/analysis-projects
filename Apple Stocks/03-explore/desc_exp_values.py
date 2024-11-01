#%%
from desc_exp_1_py import values_count, mean_values
from desc_exp_1_py import median_values, range_max_min
from desc_exp_1_py import var_dict, std_dev_dict
#%%
# Count data
print("Raw output, tables are provided further on")
print(" ")
print("---------------------------------")
print(" ")
print("Number of rows ", values_count)
print(" ")
print("---------------------------------")
print(" ")

# Means
print("Means")
print(mean_values)
print(" ")
print("---------------------------------")
print(" ")

# Medians
print("Median")
print(median_values)
print(" ")
print("---------------------------------")
print(" ")

# Range : Max + Min
print("Range: Max/Min")
print(range_max_min)
print(" ")
print("---------------------------------")
print(" ")

# Variance
print("Variance")
print(var_dict)
print(" ")
print("---------------------------------")
print(" ")

# Standard Deviations
print("Standard Deviation")
print(std_dev_dict)
print(" ")
print("---------------------------------")
print(" ")
#%%
import pandas as pd
mean_frame = pd.DataFrame(list(mean_values.items()), columns=['Key', 'Values'])
mean_frame
#%%
median_frame = pd.DataFrame(list(median_values.items()), columns=['Key', 'Values'])
median_frame
#%%
range_frame = pd.DataFrame(list(range_max_min.items()), columns=['Key', 'Values'])
range_frame
#%%
var_frame = pd.DataFrame(list(var_dict.items()), columns=['Key', 'Values'])
var_frame
#%%
SD_frame = pd.DataFrame(list(std_dev_dict.items()), columns=['Key', 'Values'])
SD_frame
#%%
