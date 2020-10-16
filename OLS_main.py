import statistics
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn import preprocessing
import scipy.stats as stats
from statistics import mean,stdev
from statsmodels.graphics.gofplots import qqplot
import math
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn import preprocessing
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


x = data[['powerPS']].values.astype(float)

# Create a minimum and maximum processor object
min_max_scaler = preprocessing.MinMaxScaler()

# Create an object to transform the data to fit minmax processor
x_scaled = min_max_scaler.fit_transform(x)

# Run the normalizer on the dataframe
norm_PPS = pd.DataFrame(x_scaled)

y = data[['price']].values.astype(float)

# Create a minimum and maximum processor object
min_max_scaler = preprocessing.MinMaxScaler()

# Create an object to transform the data to fit minmax processor
y_scaled = min_max_scaler.fit_transform(y)

# Run the normalizer on the dataframe
norm_price = pd.DataFrame(y_scaled)


# Scatter plot
plt.scatter(norm_PPS[0], norm_price[0])

# Estimate the linear regression parameters using the normalised powerPS and price
a,b = estimate_coef(norm_PPS[0], norm_price[0])
a,b

# Uses the method of least squares to plot the line of best fit
plot_regression_line (norm_PPS[0], norm_price[0], a, b)

# Hypothesis testing :
# Null hypothesis (H0): powerPS and price are independent.
# Alternate hypothesis (H1): powerPS and price dependent.
data1 = data.powerPS
data2 = data.price
stat, p = pearsonr(data1, data2)
print('stat = ',stat,', p = ',p)
if p > 0.05:
    print('Failed to reject H0')
else:
    print('Reject H0')

# Calculating the correlation (Pearson's) between price and the power per stroke
corr, _ = pearsonr(data.price, data.powerPS)
corr