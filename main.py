"""
    PROGRAM TITLE: Stock Market Simulation
    WRITTEN BY: James Hill
    DATE WRITTEN: December, 2020
    WRITTEN FOR: Personal Project
    PROGRAM INTENT: This is a program that will simulate the random price
    fluctuations of the stock market over the course of one quarter, here
    defined as an average of 63 working days in a three-month period.


"""

# import necessary modules
import random
import matplotlib.pyplot as plt

# Initialize Variables
priceIndex = 250  # Value at close of business
indexPriceChange = 0  # Change in value
trend = 1  # Positive or Negative trend in value change. 1=Positive, 0=Negative
day = 0
reverse = "no"  # change in trend

# Initialize Lists to contain data for matplotlab
days = []
index = []

# Begin Simulation Loop
while day < 63:
    day = day + 1

    # Determine if the daily trend remains the same or changes
    trendChange = random.randint(0, 100)
    if trendChange > 25:
        reverse = "no"
    # If the daily trend changes, then the value of variable 'trend' adjusts
    # to trigger the correct calculation below
    if trendChange <= 25:
        reverse = "yes"
        if trend == 1:
            trend = 0
        elif trend == 0:
            trend = 1

    # Calculate change to price index
    # Daily change is added or subtracted based on positive or negative trend.
    if reverse == "no":
        indexPriceChange = random.randint(0, 25)
        if trend == 1:
            priceIndex = priceIndex + indexPriceChange
        if trend == 0:
            priceIndex = priceIndex - indexPriceChange

    if reverse == "yes":
        indexPriceChange = random.randint(0, 100)
        if trend == 1:
            priceIndex = priceIndex + indexPriceChange
        if trend == 0:
            priceIndex = priceIndex - indexPriceChange

    # Output Results
    # print (day, trendChange,reverse, trend, priceIndex) #output test
    days.append(day)
    index.append(priceIndex)

# Graph the changes in the Price Index
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(days, index, c='red', alpha=0.5)

# Format plot
ax.set_title("Simulated Stock Market Price Index: One Quarter", fontsize=20)
ax.set_xlabel('Working Days', fontsize=16)

ax.set_ylabel("Price Index in USD", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
