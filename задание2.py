cube_array = []
summ_array = 0
for num in range(1, 1000, 2):
    cube_array.append(num**3)
for num in range(1, 500):
    temp = cube_array[num]
    digit_summ = 0
    while temp > 0:
        digit = temp % 10
        digit_summ += digit
        temp = temp // 10
    if digit_summ % 7 == 0:
        summ_array += cube_array[num]
print(summ_array)
for num in range(1, 500):
    cube_array[num] += 17
summ_array = 0
for num in range(1, 500):
    temp = cube_array[num]
    digit_summ = 0
    while temp > 0:
        digit = temp % 10
        digit_summ += digit
        temp = temp // 10
    if digit_summ % 7 == 0:
        summ_array += cube_array[num]
print(summ_array)    