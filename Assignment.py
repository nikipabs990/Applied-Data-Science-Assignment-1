# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 00:14:59 2023

@author: pabas
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_life_expectancy(df, year_col, both_sexes_col):
    """
    This function takes in a pandas DataFrame, column names for year and life expectancy, and 
    plots a line graph of life expectancy over time for each location in the dataset.
    """

    # Group the data by location
    grouped_data = df.groupby('Location')

    # Plot a line graph for each location
    for name, group in grouped_data:
        plt.plot(group[year_col], group[both_sexes_col], label=name)

    # Add chart titles and labels
    plt.title('Life Expectancy Over Time')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.legend()

    # Show the plot
    plt.show()


def plot_life_expectancy_by_gender(df, location, year_col, male_col, female_col):
    """
    This function takes in a pandas DataFrame, a location, and column names for year, male life expectancy,
    and female life expectancy. The function plots a bar chart of male and female life expectancy over time
    for the specified location.
    """

    # Filter data for the given location
    df_location = df[df['Location'] == location]

    # Plot a bar chart for male and female life expectancy
    fig, ax = plt.subplots()
    ax.bar(df_location[year_col] - 0.2, df_location[male_col],
           width=0.4, align='center', label='Male')
    ax.bar(df_location[year_col] + 0.2, df_location[female_col],
           width=0.4, align='center', label='Female')
    ax.set_xticks(df_location[year_col])
    ax.set_xlabel('Year')
    ax.set_ylabel('Life expectancy')
    ax.set_title(f'Life expectancy in {location} by gender')
    ax.legend()
    plt.show()


def plot_pie_chart(df_life_ex, year):
    """
    This function takes in a pandas DataFrame and a year. It filters the DataFrame for the given year and
    plots a pie chart of the percentage of life expectancy for both sexes by location.
    """

    # filter for the given year
    df = df_life_ex[df_life_ex['Year'] == year]

    # plot pie chart for Both Sexes column
    labels = df['Location']
    sizes = df['Both Sexes']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

    # add legend to top right corner
    plt.legend(title='Location', loc='upper right', bbox_to_anchor=(1.3, 1))

    # add title
    plt.title('Both Sexes Percentage in {}'.format(year))

    # show plot
    plt.show()


df_life_ex = pd.read_excel(
    "C:/Users/pabas/OneDrive/Healthy Life Expectancy(HALE) at age 60 (years).xlsx")
print(df_life_ex)

plot_life_expectancy(df_life_ex, 'Year', 'Both Sexes')

plot_life_expectancy_by_gender(df_life_ex, 'Africa', 'Year', 'Male', 'Female')

plot_pie_chart(df_life_ex, 2015)