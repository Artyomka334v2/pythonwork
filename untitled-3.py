# -*- coding: utf-8 -*-
array = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
name = ""
for el in array:
    name = ""
    for i in range(len(el)-1, 0 , -1):
        if el[i] != " ":
            name += el[i]
        else: 
            break
    name = name[::-1]
    name = name.capitalize() 
    hello = "Привет, " + name + "!"
    print(hello)
        