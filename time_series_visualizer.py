import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data 
df = pd.read_csv('fcc-forum-pageviews.csv')
df = df.set_index('date')
# Clean data
df = df[
    (df['value'] >= (df['value'].quantile(0.025))) & 
    (df['value'] <= (df['value'].quantile(0.975)))   
    ]
df.index = pd.to_datetime(df.index)


def draw_line_plot():
    
# Draw line plot
    fig = plt.figure(figsize=(15,10))
    plt.plot(df.index, df['value'],color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['Years'] = [d.year for d in df_bar.date]
    df_bar['Months'] = [d.strftime('%b') for d in df_bar.date]
    df_bar = df_bar.groupby(["Years", "Months"])["value"].mean()
    df_bar = df_bar.unstack()
    clist_new = ["Jan","Feb", "Mar", "Apr", "May","Jun","Jul","Aug", "Sep","Oct","Nov","Dec"]
    df_bar = df_bar[clist_new]
    
    # Draw bar plot
    fig = df_bar.plot(kind ="bar", legend = True, figsize = (15,10)).figure
    plt.xlabel("Years", fontsize= 10)
    plt.ylabel("Average Page Views", fontsize= 10)
    plt.legend(fontsize = 10, title="Months",labels=["January","February", "March", "April", "May","June","July","August", "September","October","November","December"])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box = df_box.rename(columns={'year': 'Year', 'month': 'Month', 'value': 'Page Views'})
    hue_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, axes = plt.subplots(1, 2, figsize=(20,10))
    sns.boxplot(x='Year', y='Page Views', data=df_box, ax=axes[0]).set(title='Year-wise Box Plot (Trend)')
    sns.boxplot(x='Month', y='Page Views', data=df_box,ax=axes[1], order=hue_order).set(title='Month-wise Box Plot (Seasonality)')
    plt.autoscale(tight=False)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig