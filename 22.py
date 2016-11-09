def score(s):
    scores = [ord(c) - ord('A') + 1 for c in list(s)]
    return sum(scores)

names_str = open('p022_names.txt').read()
names = names_str.split(',')
names.sort()
names = [name[1:-1] for name in names]

ssum = 0
for i in range(0, len(names), 1):
    ssum += (i+1) * score(names[i])

print(ssum)
