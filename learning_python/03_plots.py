
#import plotly.express as px ... plotly doesn't seem to work, but I get the impression it's better? can interface with js?
import plotly.express as px
import matplotlib.pyplot as plt

hours = pd.read_csv('https://raw.githubusercontent.com/Bikingman/Impact_of_weather_on_ridership/master/learning_python/data/hour.csv')
days = pd.read_csv('https://raw.githubusercontent.com/Bikingman/Impact_of_weather_on_ridership/master/learning_python/data/day.csv')

#https://www.machinelearningplus.com/plots/matplotlib-tutorial-complete-guide-python-plot-examples/
try:
    x = hours.loc[:,'cnt']
    y = hours.loc[:,'temp']
    plt.scatter(x, y)
except OSError:
    print("Why?")

try:
    x = hours.loc[:,'cnt']
    y = hours.loc[:,'hum']
    plt.scatter(x, y)
except OSError:
    print("Why?")

# Scatter Plot
fig = plt.figure(figsize=(14, 7), dpi= 80, facecolor='w', edgecolor='k')
plt.scatter('temp', 'cnt', data=days, c='temp', cmap='Reds', edgecolors='black', linewidths=.5) #add in size with s = ''
plt.title("Scatter Plot of Daily Bike Hires vs Tempurature \n(color: 'cnt' is numeric column)", fontsize=16)
plt.xlabel('Hour', fontsize=18)
plt.ylabel('Count', fontsize=18)
plt.colorbar()
plt.show()



# Scatterplot
#https://www.machinelearningplus.com/plots/matplotlib-tutorial-complete-guide-python-plot-examples/
# take some time recreate thsi with bikeshare data
import numpy as np
from numpy.random import seed, randint
seed(100)

# Setup the subplot2grid Layout
fig = plt.figure(figsize=(10, 5))
ax1 = plt.subplot2grid((2,4), (0,0))
ax2 = plt.subplot2grid((2,4), (0,1))
ax3 = plt.subplot2grid((2,4), (0,2))
ax4 = plt.subplot2grid((2,4), (0,3))
ax5 = plt.subplot2grid((2,4), (1,0), colspan=2)
ax6 = plt.subplot2grid((2,4), (1,2))
ax7 = plt.subplot2grid((2,4), (1,3))

# Input Arrays
n = np.array([0,1,2,3,4,5])
x = np.linspace(0,5,10)
xx = np.linspace(-0.75, 1., 100)

# Scatterplot
ax1.scatter(xx, xx + np.random.randn(len(xx)))
ax1.set_title("Scatter Plot")

# Step Chart
ax2.step(n, n**2, lw=2)
ax2.set_title("Step Plot")

# Bar Chart
ax3.bar(n, n**2, align="center", width=0.5, alpha=0.5)
ax3.set_title("Bar Chart")

# Fill Between
ax4.fill_between(x, x**2, x**3, color="steelblue", alpha=0.5);
ax4.set_title("Fill Between");

# Time Series
dates = pd.date_range('2018-01-01', periods = len(xx))
ax5.plot(dates, xx + np.random.randn(len(xx)))
ax5.set_xticks(dates[::30])
ax5.set_xticklabels(dates.strftime('%Y-%m-%d')[::30])
ax5.set_title("Time Series")

# Box Plot
ax6.boxplot(np.random.randn(len(xx)))
ax6.set_title("Box Plot")

# Histogram
ax7.hist(xx + np.random.randn(len(xx)))
ax7.set_title("Histogram")

fig.tight_layout()




#plot with two axis
# Import Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/economics.csv")
x = df['date']; y1 = df['psavert']; y2 = df['unemploy']

# Plot Line1 (Left Y Axis)
fig, ax1 = plt.subplots(1,1,figsize=(16,7), dpi= 80)
ax1.plot(x, y1, color='tab:red')

# Plot Line2 (Right Y Axis)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.plot(x, y2, color='tab:blue')

# Just Decorations!! -------------------
# ax1 (left y axis)
ax1.set_xlabel('Year', fontsize=20)
ax1.set_ylabel('Personal Savings Rate', color='tab:red', fontsize=20)
ax1.tick_params(axis='y', rotation=0, labelcolor='tab:red' )

# ax2 (right Y axis)
ax2.set_ylabel("# Unemployed (1000's)", color='tab:blue', fontsize=20)
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.set_title("Personal Savings Rate vs Unemployed: Plotting in Secondary Y Axis", fontsize=20)
ax2.set_xticks(np.arange(0, len(x), 60))
ax2.set_xticklabels(x[::60], rotation=90, fontdict={'fontsize':10})
plt.show()
