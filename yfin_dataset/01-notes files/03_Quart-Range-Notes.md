# Observations

The notes on this page provide an analysis of data computed in **yfin_group_range_desc.ipynb**, results for which are also copied at the bottom of this page. 

There is a lot going on in the data so we will work through each point and develop next steps one-by-one. First we will go over what was already documented after looking at median values, then we will look at the range statistics more closely.

## Medians and quartiles

- We saw Lowest score in the 1st quartile and highest scores in the 4th quartile range from 2.10 to 4369.58
- We also saw that in either direction this is a large departule from the mean
- However, the departure in the upward direction was significantly greater (qualitatively speaking)
- We saw that looking at the highest score in the 1st and lowest in the 4th validates this

In other words the data seem to corrborate the idea that there is both a lot of variability in the data and that there are outlier.  

## Range statistics

To explore this a little more fully we took an unconventional approach; we defined a column for daily range, grouped this data by company and then computed mean, min, max and standard deviation in order to explore how individual companies might be contributing to the data's shape. The results confirm the idea that some companies contribute to the variability significantly more than others. 

### Differences in range

First, let us observe that the mean range scores vary from between 0.04 to 119.99, that companies std. deviations for the range also vary (0.01 to 58.82) and that we have a highest maximum range of 657 and a lowest minimum of 0.04). These values suggest that while some companies values remain consistent over time, there are companies on the other end of the spectrum that can be classified differently. 

### Volatility and stability

Based on these observations, we can conclude that there are at least two classifications to consider as entry points for further analysis, those that are volatile and those that have long-term stability. This classification may be a rationale for a number of apporaches to the data, especially for tests that assume normality.  

### Contextual and/or dynamic factors

One consideration coming from the results is the role of either contextual factors (not in the data set themselves) having an influence as well as dynamic factors that might be inferred from the right kind of analysis. 

With respect to the former, LYG (Lloyd's Group) shows little variation and is a well established bank. NVR specializes in housing and finance and seems to have risen in value by a very large amount in the last five years, possibly connected to the housing market or developments in the states it is present. 

With respect to dynamics, we might find patterns such as patterns of change, changes that are predictive of other changes or some other structural features not yet evident in the analysis. 

## Further analysis

The approach taken here provides its own opportunities for analysis. first we will discuss these and then analyses we will drive towards as we progress with the data.

### Analysis on quartiles and ranges

To begin, reassessing mean and median scores after removing outliers will help use methods that assume a normal distribution. It will be interesting to see if the removed companies share any characteristics. 

It will also be interesting to remove data with significantly extreme ranges of values. This data may itself create a risk of type 2 error.  

Finally, creating a data-frame with the outputs of the analysis discussed here and starting a new analysis could be fruitful. This may not only reveal patterns otherwise not identified. In particular, it will be interesting to use the data on range to see how this relates to price behavior. 

### Further analysis in general

#### Cleaning data (next steps)
- Identify and remove outliers
- Create variable for data with and without high range companies
- Reevaluate skew

#### Correlation
- Correlations to see how data on range correlates with price
- Correlations to see how Open and Close prices compare, especially with range as it is defined here
- Correlation to see how range correlates with the mean value of a company over time

#### Interactions
- ANOVA (will probably need to create some new variables or new data table)

#### Structure 
- Factor Analysis (Find dimensions/underlying structure) 
- Structural Equation Modeling (Find underlying structure/hidden variables | **library**: https://semopy.com/)

We will start with correlations and continue to make observations as we go. FiRst however, we will create some graphical outputs to help visualize our findings.
