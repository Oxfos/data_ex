import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/los_altos_2019.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        high = int(row[8])
        low = int(row[9])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
    # Convert Farenheit to Celsius.
    highs = [(t-32)*5/9 for t in highs]
    lows = [(t-32)*5/9 for t in lows]

    # Plot the high temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    plt.title("Daily high and low temperatures, 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (C)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()