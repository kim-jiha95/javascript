def f(): return map(int, input().split())


n, m = f()
que = [*range(1, n+1)]
ix, cnt = 0, 0
for _ in f():
    q = que.index(_)
    m1 = abs(q-ix)
    m2 = len(que) - m1
    cnt += min(m1, m2)
    ix = q
    del que[q]
print(cnt)
