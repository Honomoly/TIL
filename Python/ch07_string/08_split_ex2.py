sum = 0

str_data = "{a1 : 20}, {a2 : 30}, {a3 : 15}, \
            {a4 : 50}, {a5 : -15}, \
            {a6 : 80}, {a7 : 0}, {a8 : -110}"

str_data_sp1 = str_data.split(',')

for data in str_data_sp1:
    data = data.split(':')
    data = data[1]
    sum += int(data[:-1])

print(sum)