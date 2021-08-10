t = int(input())


for i in range(t):
    num, word = input().split()
    for x in word:
        print(x * int(num), end='')
    print()
