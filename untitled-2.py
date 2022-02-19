# -*- coding: utf-8 -*-
array = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_array = []
for el in array:
    temp = el[0]
    if (ord(temp) > 42) and (ord(temp) <= 58):
        new_array.append('"')
        if len(el) < 2:
            new_array.append("0"+el)
        elif (ord(temp) > 42) and (ord(temp) < 48) and (len(el) == 2):
            new_array.append(temp + "0" + el[-1])
        else:
            new_array.append(el)
        new_array.append('"')
    else:
        new_array.append(el)
final_string = ""
ident = 1
for el in new_array:
    if (el == '"') and (ident % 2 == 0):
        final_string += el
        final_string += " "
        ident += 1
    elif (el == '"') and (ident % 2 != 0):
        final_string += el
        ident += 1
    elif (ord(el[0]) > 42) and (ord(el[0]) <= 58):
        final_string += el
    else:
        final_string += el
        final_string += " " 
print(final_string)