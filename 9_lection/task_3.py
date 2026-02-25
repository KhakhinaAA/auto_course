import re
# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases
# Здесь пишем код

file = open(r'C:\Users\user\project_auto\9_lection\test_file\task_3.txt', mode='r', encoding='utf-8')
file_1 = file.read()
file_1_2 = file_1.split('\n\n')
# print(file_1_2)
file.close()
list_sum = []
for i in range(len(file_1_2)):
    lines = re.findall(r"\d+", file_1_2[i])
    # print(lines)
    lines = [int(item) for item in lines]
    sum_lines = sum(lines)
    list_sum.append(sum_lines)
print(list_sum)
summa = sorted(list_sum)
top_3_max = summa[-3:]
three_most_expensive_purchases = sum(top_3_max)
print(three_most_expensive_purchases)
assert three_most_expensive_purchases == 202346
