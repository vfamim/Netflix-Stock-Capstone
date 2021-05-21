# NETFLIX STOCK PRICES

############################
# 0.0. IMPORT DATA
############################

# %%
# data manipulation
import pandas as pd

# data visualization
import matplotlib.pyplot as plt
import seaborn as sns

############################
# 1.0. DATA
############################

# 1.1. loading data
# %%
netflix_stock = pd.read_csv(
    'data/NFLX.csv', parse_dates=['Date'], index_col='Date')
netflix_stock_quartely = pd.read_csv(
    'data/NFLX_daily_by_quarter.csv', parse_dates=['Date'], index_col='Date')
djow_stock = pd.read_csv(
    'data/DJI.csv', parse_dates=['Date'], index_col='Date')
print(netflix_stock.head())
print('---' * 20)
print(netflix_stock_quartely.head())
print('---' * 20)
print(djow_stock.head())

############################
# 1.1. INSPECT DATA
############################

# info
# %%
print(netflix_stock.info(show_counts=True), netflix_stock_quartely.info(show_counts=True),
      djow_stock.info(show_counts=True))
print(netflix_stock.describe(), netflix_stock_quartely.describe(),
      djow_stock.describe())

############################
# 1.2. ADJUST DATA
############################

# rename
# %%
netflix_stock.rename(
    columns={'Adj Close': 'Price'},
    inplace=True)
netflix_stock_quartely.rename(
    columns={'Adj Close': 'Price'},
    inplace=True)
djow_stock.rename(
    columns={'Adj Close': 'Price'},
    inplace=True)

# time series
# %%
# months
netflix_stock['Month'] = netflix_stock.index.month_name()
netflix_stock_quartely['Month'] = netflix_stock_quartely.index.month_name()
djow_stock['Month'] = djow_stock.index.month_name()

# quarter
# %%
netflix_stock['Quarter'] = netflix_stock.index.quarter
djow_stock['Quarter'] = djow_stock.index.quarter

############################
# 2.0. DATA ANALYSIS
############################

# violinplot
# %%
sns.violinplot(data=netflix_stock_quartely, x='Quarter', y='Price')
plt.title('Distribution of 2017 Netflix Stock Prices by Quarter')
plt.ylabel('Closing Stock Price')
plt.xlabel('Business Quarters in 2017')
plt.show()

# revenue x earnings
# %%
# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98, 3.29, 3.7]
earnings_by_quarter = [.0656, .12959, .18552, .29012]
quarter_labels = ["2Q2017", "3Q2017", "4Q2017", "1Q2018"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2  # Number of dataset
d = 4  # Number of sets of bars
w = 0.8  # Width of each bar
bars1_x = [t*element + w*n for element
           in range(d)]

# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2  # Number of dataset
d = 4  # Number of sets of bars
w = 0.8  # Width of each bar
bars2_x = [t*element + w*n for element
           in range(d)]

middle_x = [(a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]
plt.bar(bars1_x, revenue_by_quarter)
plt.bar(bars2_x, earnings_by_quarter)
plt.legend(labels)
plt.title('Revenue x Earnings')
plt.xticks(middle_x, quarter_labels)
plt.show()

# actual x estimate
# %%
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017", "2Q2017", "3Q2017", "4Q2017"]
earnings_actual = [.4, .15, .29, .41]
earnings_estimate = [.37, .15, .32, .41]

# Ploting
plt.scatter(x_positions, earnings_actual, color='red', alpha=0.5)
plt.scatter(x_positions, earnings_estimate, color='blue', alpha=0.5)
plt.legend(['Actual', 'Estimate'])
plt.xticks(x_positions, chart_labels)
plt.show()
