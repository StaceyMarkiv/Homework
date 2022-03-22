table_1 = []
for i in range(1, 10):
    table_2 = []
    for j in range(1, 10):
        table_2.append(i*j)
    table_1.append(table_2)
count = 0
for t in table_1:
    count += 1
    print(f'Умножение на {count}: {t}')
print('\n')

table_3 = []
for i in range(1, 10):
    table_4 = []
    for j in range(1, 10):
        i += i
        table_4.append(i)
    table_3.append(table_4)
count = 0
for t in table_1:
    count += 1
    print(f'Умножение на {count}: {t}')
