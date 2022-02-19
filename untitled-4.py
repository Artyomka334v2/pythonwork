# -*- coding: utf-8 -*-
price = [51.8, 61.4, 1.55, 3, 1000, 28.03]
for el in sorted(price):
    rub = int(el)
    k = int((el * 100) % 100)
    if (k < 10):
        final_price = str(rub) + " руб " + "0" + str(k) + " коп"
    else:
        final_price = str(rub) + " руб " +  str(k) + " коп"
    print(final_price, end="; ")
print()
price_sort = sorted(price, reverse=True)
for el in price_sort:
    rub = int(el)
    k = int((el * 100) % 100)
    if (k < 10):
        final_price = str(rub) + " руб " + "0" + str(k) + " коп"
    else:
        final_price = str(rub) + " руб " +  str(k) + " коп"
    print(final_price, end="; ") 
print()
for i in range(0, 5):
    print(price_sort[i], end="; ")
    
    
    