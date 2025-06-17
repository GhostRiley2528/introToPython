#zip the elements 
s1 = [1, 2, 3]
s2 = [4, 5, 6]
s3 = list(zip(s1, s2))

list1 = [10, 20, 30]
list2 = [400, 500, 600]

for x, y in zip(list1, list2):
    print(x, y)

stocks = ['sensex', 'nifty', 'banknifty']
prices = [50000, 15000, 35000]

new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}

print('\n{}'.format(new_dict))