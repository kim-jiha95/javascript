# dfs를 활용해서 풀었다.

# cnt변수를 global로 선언해주고, 현재 방문한 좌표에 '0'을 대입한다.
# for 문으로 상,하,좌,우 4번 반복해서 현재 비교중인 좌표가 1인 경우 다시 dfs재귀호출, 만약 1이 아니라면 for문을 탈출해서 다른 방향을 비교한다.
# ** dfs재귀호출 할때마다 cnt증가한다.

import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(sys.stdin.readline())
a = [list(sys.stdin.readline()) for _ in range(n)]
cnt = 0
apt = []


def dfs(x, y):
    global cnt
    a[x][y] = '0'  # 방문한 곳은 0으로
    cnt += 1
    for i in range(4):
        nx = x + dx[i]  # i=0일때 (nx,ny)는 좌 , i=1일때 (nx,ny)는 상
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if a[nx][ny] == '1':
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if a[i][j] == '1':
            cnt = 0
            dfs(i, j)
            apt.append(cnt)

print(len(apt))
apt.sort()
for i in apt:
    print(i)
