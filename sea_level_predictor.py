import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='blue', marker='o', edgecolor='black')

    
    # Create first line of best fit

    lineA = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    xA = np.arange(df['Year'].min(), 2051, 1)
    yA = (lineA.slope * xA) + lineA.intercept

    

    # Create second line of best fit

    df_2000 = df[df['Year'] >= 2000]

    lineB = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    xA2 = np.arange(2000, 2051, 1)
    yA2 = (lineB.slope * xA2) + lineB.intercept

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    plt.grid(True)
    plt.show()
    plt.plot(xA, yA)
    plt.plot(xA2, yA2)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()