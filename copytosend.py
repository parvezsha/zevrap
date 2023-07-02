import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
#Read the CSV file into df
datafile = pd.read_csv("lastonemonth.csv")

datafile['datetime'] = datafile['date'].astype(str) + datafile['time']

change_datetime = pd.DataFrame({'date':datafile['datetime']})
change_datetime['datetime'] =pd.to_datetime(change_datetime['date'],format='%Y%m%d%H:%M')

#candlestick plot 
plotdata = go.Figure(data=[go.Candlestick(x=change_datetime['datetime'],
                            open=datafile['open'],
                            high=datafile['high'],
                            low=datafile['low'],
                            close=datafile['close'],
                            increasing_line_color= 'green', 
                            decreasing_line_color= 'red')])

plotdata.update_layout(
    title='The Aravinthan project',
    yaxis_title='Stock',
    yaxis=dict(range=[13000,14200]),
    xaxis_title='Date/Time',
    xaxis_rangeslider_visible = False
)
plotdata.update_xaxes(
            rangebreaks=[
            dict(bounds=["sat", "mon"]),  
            dict(bounds=[15.5, 9.25], pattern="hour"), 
        ]
    )
plotdata.show()