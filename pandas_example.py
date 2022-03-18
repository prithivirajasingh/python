#!/usr/bin/env python
import pandas

data= pandas.read_csv("products.csv")     # stores the csv as dataframe
print(type(data))
print(data)
print(data.iat[0, 0])   # returns 0,0 element
print(data.shape[0])    # returns row count
print(data.shape[0])    # returns column count
exit()


productsURL = "products.csv"
products= pd.read_csv(productsURL)

products.index += 1
products = products.rename_axis('ID')
# left_aligned_products = products.style.set_properties(**{'text-align': 'left'})
# left_aligned_products
# print(type(products))
# sort = products.sort_values(products.columns[0])
print(tabulate(products, headers='keys', showindex=True, tablefmt='psql', numalign='left', floatfmt=".2f"))
# print(sort)
# print(products.to_string(header=False))
# print("{:<15} {:<15}".format(products.iloc[:, 0].to_string(index=False, header=False), products.iloc[:, 1].to_string(index=False, header=False)))
# print("{:<15} {:<15} {:<15} {:.2f}".format(products.to_string(header=False)))
print(products.iat[1, 0])
# print(products.shape[0])
exit()
