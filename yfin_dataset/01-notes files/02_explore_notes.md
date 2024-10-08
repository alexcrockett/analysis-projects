# Notes
We can see that the data has some very interesting features from the initial analysis and there are one or two areas that it will be interesting to explore further before any kind of deeper analysis.

## Descriptive statistics (observations)

**From [fin_descriptives.ipynb]** 
- The mean and the median have some distance between them. The mean is higher by double across all values (Open, Close, High, Low and Volume).

### Skewness
- mean open: 140.07
- min open: 1.05
- max open: 6490.26
- Range: 6489.21
- standard deviation: 275.4 (twice the mean)
 
In other words the data is positively skewed. This will need to be remembered for later analysis. An interesting line of further investigation would therefore be to see which of the following is influencing this skew:

- Is a particular stock responsible?
- Is a particular period of time responsible?

It will therefore be useful to group the data by company to compare some of their statistics, as well as by year. 

### Uncertain volatility
Another interesting factor are the results for the standard deviations for all scores. 

**The standard deviation**
The standard deviation is written:

$\sigma = \sqrt {\frac{\sum (x_i - \mu )^2}{N}}$ 

It tells us the degree to which values vary. What is interesting is that the standard deviation for each set of data seems to be relatively consistent, all are in the range of 275 $\pm 4$. Similarly, the means are all within the range of 140 $\pm 2$, which suggests a few possibilities:

- A standard deviation twice the mean suggests some variability
- It may also suggest some outliers

However, the consistency between Open, CLose, Low and Highs indicate low volatility. A delta of 6,523.97, which is the value of the minimum low value subtracted from the maximum high is very much almost that maximum high value. 

## Partial summary

We therefore need to do some further investigation. 

1. Produce plot to review the data
2. First we'll compute descriptive statistics for on a per-stock basis, i.e. we will look at scores for APPL and so on.
2. Once we've identified outliers, we will review statistics without the outliers.
3. We will then make some decisions about how we want to normalize the data (and in fact if we need to) for our first analysis.

For each, we will create a seperate notebook and import variables and data from our original file [fin_descriptives.ipynb].