from bsedata.bse import BSE
stock = BSE()
#print(stock)
#quote = stock.getQuote('590006')
#print(quote)
companylist = ['532215','532149','504973','533162','543458','543280']

for company in companylist:
    quote = stock.getQuote(company)
    print(quote["companyName"])
    print(quote["currentValue"])
    print(quote["updatedOn"])
    print(quote["2WeekAvgQuantity"])
    #print(quote)