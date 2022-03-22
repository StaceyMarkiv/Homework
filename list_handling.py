import random
import math
import copy

my_list = [random.randrange(20) for i in range(10)]
print(my_list)

single = []
not_single = []
list_sum = 0
list_multipl = 1
count = 0
for i in my_list:
    if my_list.count(i) != 1:
        if i not in not_single:
            not_single.append(i)
    else:
        single.append(i)
    list_sum = list_sum + i
    list_multipl = list_multipl * i
    count += 1
print(f'Встречаются более одного раза: {not_single}')
print(f'Встречаются один раз: {single}')

single1 = []
not_single1 = []
for i in range(len(my_list)):
    if (my_list[i] in my_list[: i]) or (my_list[i] in my_list[i+1:]):
        temp = True
        for j in not_single1:
            if my_list[i] == j:
                temp = False
        if temp:
            not_single1.append(my_list[i])
    else:
        single1.append(my_list[i])
print(f'Встречаются более одного раза: {not_single1}')
print(f'Встречаются один раз: {single1}')

arithm_mean = sum(my_list)/len(my_list)
print(f'Среднее арифметическое: {arithm_mean}')
arithm_mean_2 = list_sum/count
print(f'Среднее арифметическое: {arithm_mean_2}')

geom_mean = math.prod(my_list) ** (1/len(my_list))
print(f'Среднее геометрическое: {geom_mean}')
geom_mean_2 = list_multipl ** (1/count)
print(f'Среднее геометрическое: {geom_mean_2}')

my_list.sort()
print(my_list)

my_list_2 = copy.deepcopy(my_list)
sorted_list = []
while my_list_2:
    for i in my_list_2:
        if i == min(my_list_2):
            sorted_list.append(i)
            my_list_2.remove(i)
print(sorted_list)
