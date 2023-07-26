import requests
import pandas as pd

header = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9',
    'Cookie':'_ga=GA1.1.1348502623.1690352611; defaultLang=en; AKA_A2=A; nsit=7xQ-uL6XKHr1G3_Yl944ezVB; bm_mi=13D0FB6B3CE5AEDCDBF8189A7F28F31C~YAAQbNcLF3C2yXaJAQAAmiQ+kxRCUSADH5TkTwatE+p5l4KFVazhzF53W7+RWhramVaVaEWDSMF7wUank5umJAWB+kfnT+ocDx3IalUZEZZKu6Gk0Q4obnkzJ5mTgYEPorpTX0SKd53UjmQkNhsuLXx4YJ59tLXxfds+46tau1ALhJeSa4dqQtjl80kGB/yO6y9cffbtWT5doFESAyToRBEvau1HpJvbz9A3ZtmO7uky5h5kz4IiUzuQCYk5YqtW3NwHsdV8vc8mL2ok0qaOrEFb+leou0FZS8A6lJ95vpPXncAz3MX0eSFIh+OgqDvt~1; ak_bmsc=B82671C1DF1EC8027B22B79C0767C663~000000000000000000000000000000~YAAQBNcLFx6cxIaJAQAA3lc+kxRGC1q+Aq7M2oMb08esgGkG56wOwg7z+hYthVKYvXG7VYfAIi9AfsOCTb+w91DKcPAZoWQwkLZDeu5E3ASHjPs1QEVAay1Hz6/F6/M3o3KycH2NgieV0mFrTCFATRMh+KIUe3TTQLvaqBEjNzW3/5g/jjTx5FIIf+3Scm4o2KfvmODYXm2V2NCi4Szw6L2shwQY6TfQ49+jERzxcs1QGe027sooXeDQAFM3nULpeE3Bt6gFBQh7cKc8GJ46XEOq/rv32ctDqM9nxCnoUSXVLdj3c4YNhZ1lHUJJddLFDE3afy8DNxxPvfTey2y8f63Kw2SjrAD5+eCjNqkCaARxLiAuiTygpRT79pAvEkIhyzHR6oX/KkIkMl5pE12RukhXe2KQDi+Z4lHBed4AnPFE5OPKYuyY0M11im9hUXuHGWyPtWWTl0Q6341jh1QKgDRNB349YYvfmeEd/QBbWfieEqlh9OQpwTvyAZfUgFJoMp83cecjSSZAaKHpXlic; nseQuoteSymbols=[{"symbol":"BAJAJ-AUTO","identifier":null,"type":"equity"},{"symbol":"BAJAJFINSV","identifier":null,"type":"equity"},{"symbol":"ITC","identifier":null,"type":"equity"}]; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTY5MDM5Mjc5MSwiZXhwIjoxNjkwMzk5OTkxfQ.EARIqf4xquApDgkVXcXy9F_iAtAQqmODoKl31H-t2-A; RT="z=1&dm=nseindia.com&si=9922d82f-94ae-4498-bb73-e7a85d485920&ss=lkk06nmg&sl=3&se=8c&tt=s11&bcn=%2F%2F684d0d49.akstat.io%2F"; _ga_PJSKY6CFJH=GS1.1.1690392475.4.1.1690392797.59.0.0; bm_sv=56E0714D7418FEE956EC73D791C546E8~YAAQbNcLF77WyXaJAQAAOhNDkxR+8FNWOTCok8KSz+Mq+QnUa7gL6afU+jFnasHdVYqLC+EOlDTmWfnvmJxcs0Plx1F9V2rxilUY1SwzUrsL1ZCfvXDb4H8IfnlOpOoUe4+RgBIgm0auGnPn8IedgH9DjFqmBC1QlVkXriH/YZx1RPZ/0IPuQT4paDDwMGLSXOV4IG8I+Q3vP2mWlx64cQX/DRpprXxuqDBJtFT4qNn1dOAhzQ/TDbQNhAC3RyM8JSXW~1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
    }
#stockname = input("Enter Stock Name ")
#link = '"https://www.nseindia.com/api/chart-databyindex?index='+ stockname +'"'

response = requests.get(url="https://www.nseindia.com/api/chart-databyindex?index=ITCEQN",headers=header)
#response = requests.get(url= link,headers=header)
#print(response)
#print(header)
itc = pd.DataFrame(response.json()['grapthData'])
#print(itc.head())
itc.columns= ['timestamp','currentprice']
itc['timestamp'] = pd.to_datetime(itc['timestamp'],unit='ms')
#print(itc.head())
#print(itc)
print(itc.tail(1))