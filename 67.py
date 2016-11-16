rows = []
with open('p067_triangle.txt') as inputfile:
    for line in inputfile:
        rows.append(line.strip())
rows = [list(map(int, row.split(' '))) for row in rows]

for i in range(len(rows)-2, -1, -1):
    for j in range(len(rows[i])):
        rows[i][j] += max(rows[i+1][j], rows[i+1][j+1])

print(rows[0][0])
