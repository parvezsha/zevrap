import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
#Read the CSV file into df
datafile = pd.read_csv("sampleniftysmall.csv")
#changed_date = pd.DataFrame({'date':datafile['date']})
#changed_time = pd.DataFrame({'time':datafile['time']})


datafile['datetime'] = datafile['date'].astype(str) + datafile['time']

#print(datafile['datetime'].info())
#print(datafile['datetime'])

change_datetime = pd.DataFrame({'date':datafile['datetime']})
change_datetime['datetime'] =pd.to_datetime(change_datetime['date'],format='%Y%m%d%H:%M')
print(change_datetime['datetime'])


"""change_datetime = pd.DataFrame({'datetime':datafile['datetime']})
change_datetime['datetime'] =pd.to_datetime(change_datetime['datetime'],format='%Y%m%d%H:M')
print(change_datetime)"""