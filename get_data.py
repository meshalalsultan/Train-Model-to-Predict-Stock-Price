import investpy


stock_name = 'pfe'

df = investpy.get_stock_historical_data(stock=stock_name,
                                        country='United States',
                                        from_date='01/01/2010',
                                        to_date='01/01/2020')
df.to_csv(stock_name +'.csv')
