t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    ans = a+b
    print("Case #%s: %s"%(i+1, ans))