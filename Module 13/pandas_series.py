import pandas as pd

from Module13.array_manipulation import total_sum

products=['Apple','Bananas','Oranges','Grapes','Pineapples']

sales=[150,200,180,90,60]

sales_series=pd.Series(sales,index=products)
print(sales_series)

print(sales_series['Grapes'])

total_sales=sales_series.sum
print(total_sales)

best_sell=sales_series.idxmax()
print(best_sell)