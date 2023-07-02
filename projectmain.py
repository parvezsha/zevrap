import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
#Read the CSV file into df
datafile = pd.read_csv("last10.csv")
#convert merge to date column and time column from data frame 
datafile['datetime'] = datafile['date'].astype(str) + datafile['time']

#after merge convert date time object to datetime datatype
change_datetime = pd.DataFrame({'date':datafile['datetime']})
change_datetime['datetime'] =pd.to_datetime(change_datetime['date'],format='%Y%m%d%H:%M')#datetime format changed

#candlestick plot 
plotdata = go.Figure(data=[go.Candlestick(x=change_datetime['datetime'],
                            open=datafile['open'],
                            high=datafile['high'],
                            low=datafile['low'],
                            close=datafile['close'],
                            increasing_line_color= 'green',#increase plot data to green color  
                            decreasing_line_color= 'red')])#Decrease plot data to Red Color

plotdata.update_layout(
    title='The Candlestick project',#Graph Title name
    yaxis_title='Stock',#y axis title name
    yaxis=dict(range=[13000,14100]),# y axis data range
    xaxis_title='Date/Time', # x axis title namex
    ) 

plotdata.update_xaxes(
        #rangeslider_visible=True,
        rangebreaks=[
            # NOTE: Below values are bound (not single values), ie. hide x to y
            dict(bounds=["sat", "mon"]),  # hide weekends, eg. hide sat to before mon
            dict(bounds=[15.5, 9.25], pattern="hour"),  # hide hours outside of 9.15am-3.30pm
            #dict(values=["2019-12-25", "2020-12-25"])  # hide holidays (Christmas and New Year's, etc)
        ]
    )
plotdata.show()