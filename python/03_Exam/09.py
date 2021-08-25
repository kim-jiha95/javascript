# bfs를 활용해서 풀었고, 불가능한 경우를 출력하기 위해서 함수 형태로 만들었다.
# 가로, 세로 좌표와 벽을 부술 수 있는 횟수를 저장하기 위해 3차원 배열로 나타내었다.

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append([0, 0, 1])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1

    while q:
        x, y, c = q.popleft()  # 좌표와 벽을 부술 수 있는 남은 횟수
        if x == n-1 and y == m-1:
            return visited[x][y][c]

        for i in range(4):
            tx = dx[i] + x
            ty = dy[i] + y

            if 0 <= tx < n and 0 <= ty < m:
                if a[tx][ty] == '1' and c == 1:  # 벽을 한 개 부숨
                    visited[tx][ty][0] = visited[x][y][1] + 1
                    q.append([tx, ty, 0])  # c를 -1해서 저장
                elif a[tx][ty] == '0' and visited[tx][ty][c] == 0:  # 빈 방이라면
                    visited[tx][ty][c] = visited[x][y][c] + 1
                    q.append([tx, ty, c])
    return -1


n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(input()))
print(bfs())
