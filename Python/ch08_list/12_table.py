table =  [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15]]

for i in table:
    for j in i:
        print(j, end='\t')
    print()

# 양식이 안맞으면?
table =  [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14]]

rows = len(table)
cols = len(table[0])

# 오류 뜸
for row in range(rows):
    for col in range(cols):
        print(table[row][col], end='\t')
    print()