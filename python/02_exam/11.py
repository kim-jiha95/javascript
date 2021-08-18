n, p = map(int, input().split())

# [line, fret]
melody = [list(map(int, input().split())) for _ in range(n)]
# 줄별로 누른 프렛 저장할 리스트
pressedLine = [[] for _ in range(7)]

move = 0  # 움직인 횟수

for line, fret in melody:
    # 줄이 비었거나 프렛이 줄 맨 마지막 값보다 큰 경우
    if not pressedLine[line] or pressedLine[line][-1] < fret:
        # 프렛 누르고 움직인 횟수 1 증가
        pressedLine[line].append(fret)
        move += 1
        continue

    # 프렛이 줄의 맨 앞 값보다 작은 경우
    if fret < pressedLine[line][0]:
        # 손가락을 모두 뗀 후 이번 순서 프렛을 리스트로 저장
        move += len(pressedLine[line]) + 1
        pressedLine[line] = [fret]
        continue

    # 이번 순서 프렛이 저장된 프렛들 사이에 있을 경우
    cnt = 0			# 줄에서 뗄 손가락 수
    # 이번 순서 프렛의 위치 찾고 뗄 손가락 수 구함.
    for i in range(1, len(pressedLine[line]) + 1):
        if pressedLine[line][-i] <= fret:
            cnt = i - 1
            break

    move += cnt			# 뗄 손가락 수 만큼 움직임 횟수 증가
    if cnt != 0:		# 떼야하는 손가락이 있다면 손가락 뗌
        pressedLine[line] = pressedLine[line][:-cnt]

    # 누른 손가락 중 마지막 손가락이 이번 순서 프렛과 같지 않다면
    # 이미 이번 순서 프렛을 누르고 있는 경우가 존재하는데, 이런 경우를 제외한 것임.
    if pressedLine[line][-1] != fret:
        # 프렛 누르고 움직임 횟수 1 증가.
        pressedLine[line].append(fret)
        move += 1

print(move)
