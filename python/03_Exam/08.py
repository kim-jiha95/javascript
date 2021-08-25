import sys
from collections import deque
height, width = map(int, sys.stdin.readline().split())
maps = []
waters = []
for y in range(height):
    arr = sys.stdin.readline()
    for x in range(len(arr)):
        if arr[x] == 'S':
            # 시작 지점
            start = [(y, x)]
        elif arr[x] == "D":
            end = (y, x)
        elif arr[x] == '*':
            # 물 시작지점
            waters.append((y, x))
    maps.append(list(arr))


def bfs(start, maps):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    queue.extend(start)

    # 시간별 다음 이동경로를 반환하도록.
    nexts = []
    while queue:
        y, x = queue.popleft()
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < height and 0 <= nx < width:
                # 물로 bfs를 돌 때. 고슴도치가 도착할 수 있는 지점이어도 물로 바꿔준다.
                if (maps[ny][nx] == "." or maps[ny][nx] == "S") and maps[y][x] == "*":
                    maps[ny][nx] = "*"
                    nexts.append((ny, nx))
                # 고슴도치가 사방으로 전진할 때.
                elif maps[ny][nx] == "." and maps[y][x] == "S":
                    maps[ny][nx] = "S"
                    nexts.append((ny, nx))
                # 목적지에 도착했을 때.
                elif maps[ny][nx] == 'D' and maps[y][x] == 'S':
                    return True
    return nexts


time = 0
while True:
    time += 1
    # 고슴도치의 이동경로 먼저 계산
    start = bfs(start, maps)

    # 물의 이동경로 계산
    waters = bfs(waters, maps)
    # 이미 D까지 도착했을 경우
    if start == True:
        print(time)
        break
    # 고슴도치가 갈 수 있는 경로가 없는 경우
    elif start == []:
        print("KAKTUS")
        break
    # waters로 한번 돌고 나면,
    # 원래 고슴도치가 있던 공간인데 물이 차서 더 이상 쓸 수 없는 지점이 있을 수 있다.
    temp = []
    for y, x in start:
        if maps[y][x] == 'S':
            temp.append((y, x))
    start = temp
