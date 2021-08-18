import sys
from collections import deque


n = int(sys.stdin.readline())
ex = deque()
ex.extend(list(sys.stdin.readline().rstrip()))
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

tmp = []
res = 0
while ex:
    x = ex.popleft()
    if x == '+' or x == '-' or x == '*' or x == '/':
        a = tmp.pop()
        b = tmp.pop()

        if str(a).isalpha():
            a = num[ord(a)-ord('A')]
        if str(b).isalpha():
            b = num[ord(b)-ord('A')]

        if x == '+':
            res = b + a
        elif x == '-':
            res = b - a
        elif x == '*':
            res = b * a
        else:
            res = b / a

        tmp.append(res)

    else:
        tmp.append(x)

print('%.2f' % res)
