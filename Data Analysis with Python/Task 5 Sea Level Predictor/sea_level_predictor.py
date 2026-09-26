import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sea_level_df = pd.read_csv('epa-sea-level.csv')
 
    # data integrity check: the rest of this function depends on these two columns
    required_columns = {'Year', 'CSIRO Adjusted Sea Level'}
    missing_columns = required_columns - set(sea_level_df.columns)
    if missing_columns:
        raise ValueError(f"epa-sea-level.csv is missing expected columns: {missing_columns}")
 
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(sea_level_df['Year'], sea_level_df['CSIRO Adjusted Sea Level'])
 
    # Create first line of best fit
    full_fit = linregress(sea_level_df['Year'], sea_level_df['CSIRO Adjusted Sea Level'])
    years_full_range = pd.Series(range(1880, 2051))
    sea_level_full_pred = full_fit.intercept + full_fit.slope * years_full_range
    ax.plot(years_full_range, sea_level_full_pred, 'r')
 
    # Create second line of best fit
    recent_df = sea_level_df[sea_level_df['Year'] >= 2000]
    recent_fit = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    years_recent_range = pd.Series(range(2000, 2051))
    sea_level_recent_pred = recent_fit.intercept + recent_fit.slope * years_recent_range
    ax.plot(years_recent_range, sea_level_recent_pred, 'green')
 
    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
 
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()