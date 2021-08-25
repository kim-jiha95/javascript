# 현재 층을 큐에 삽입한 후 상, 하로 움직이면서 목표층에 도달할 수 있는지 파악한다.
# 도달하는 경우 움직인 최솟값을 출력한다
# 도달하지 못하는 경우 use the stairs를 출력

from collections import deque


def bfs(F, S, G, U, D):
    q = deque([[S, 0]])
    visited = {S}

    while q:
        floor, cnt = q.popleft()
        if floor == G:  # 목표 층에 도착
            return cnt
        if floor + U <= F and floor + U not in visited:  # 위층으로 이동
            q.append([floor + U, cnt + 1])
            visited.add(floor + U)
        if floor - D >= 1 and floor - D not in visited:  # 아래층으로 이동
            q.append([floor - D, cnt + 1])
            visited.add(floor - D)

    return "use the stairs"


if __name__ == "__main__":

    F, S, G, U, D = map(int, input().split())

    print(bfs(F, S, G, U, D))
