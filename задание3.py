## -*- coding: utf-8 -*-
for num in range(1, 101):
    if (num % 10 == 1) and ((num == 1) or (num > 20)):
        print(num, "процент")
    elif ((num % 10 == 2) or (num % 10 == 3) or (num % 10 == 4)) and ((num < 10) or (num > 20)):
        print(num, "процента")
    else:
        print(num, "процентов")