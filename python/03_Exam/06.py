# 동서남북 4방향 뿐만 아니라 상하까지 고려하여 이동 좌표를 설정한다
# 시작 지점에서 E에 도착할 때까지 bfs를 수행한 후 조건에 맞게 출력

from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(x, y, z):
    q.append([x, y, z])
    d[x][y][z] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if a[nx][ny][nz] == 'E':
                    print("Escaped in {0} minute(s).".format(d[x][y][z]))
                    return
                if a[nx][ny][nz] == '.' and d[nx][ny][nz] == 0:
                    d[nx][ny][nz] = d[x][y][z] + 1
                    q.append([nx, ny, nz])
    print("Trapped!")


while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    a = [[[]*c for _ in range(r)] for _ in range(l)]
    d = [[[0]*c for _ in range(r)] for _ in range(l)]
    q = deque()
    for i in range(l):
        a[i] = [list(map(str, input().strip())) for _ in range(r)]
        input()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if a[i][j][k] == 'S':
                    bfs(i, j, k)
