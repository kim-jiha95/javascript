from itertools import permutations

n = int(input())
lst = []

for i in range(1, n+1):
    lst.append(i)

result = list(permutations(lst, n))
for i in result:
    for j in i:
        print(j, end=' ')
    print()
