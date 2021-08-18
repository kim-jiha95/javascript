from collections import Counter

N = int(input())
pillar = [list(map(int, input().split())) for _ in range(N)]  # 기둥. [위치, 높이]
pillar.sort(key=lambda x: x[0])			# 위치 기준으로 오름차순 정렬

max_height = max(pillar, key=lambda x: x[1])[1]  # 가장 큰 기둥 높이
height_count = Counter(list(zip(*pillar))[1])  # 기둥의 높이 별 개수
max_height_num = height_count[max_height]  # 가장 큰 높이를 가진 기둥의 개수.
area = 0					# 면적
x, y = pillar[0][0], 0				# 좌표 초기화

for i in range(len(pillar)):			# 정렬된 기둥들을 차례로 가져와 반복문 실행
    p = pillar[i]
    if max_height_num > 0:		# 가장 큰 높리를 가진 기둥을 다 지나지 않은 경우. 지붕 상승 또는 유지
        if p[1] >= y:				# 현재 기둥이 직전 기둥보다 크거나 같은 경우
            area += (p[0] - x) * y  # 직전 기둥과 현재 기둥 사이의 면적을 구해 area에 더함
            x = p[0]				# x, y 좌표 최신화
            y = p[1]
        if p[1] == max_height:			# 현재 기둥이 가장 큰 기둥인 경우
            area += y			# 기둥이 위치한 면적 더함. 위 그림에서는 8~9 사이의 면적
            x += 1				# x 좌표 1 증가
            max_height_num -= 1			# 가장 큰 기둥을 1 뺀다.
    else:					# 전체에서 가장 큰 기둥은 지나감.
        # 현재 기둥 포함 이후 가장 큰 기둥의 높이를 대입
        max_height = max(pillar[i:], key=lambda x: x[1])[1]
        if max_height == p[1]:			# 현재 기둥이 가장 크다면
            y = p[1]				# y w 좌표 최신화
            area += (p[0] - x + 1) * y		# 현재 기둥까지의 면적 더해줌
            x = p[0] + 1			# x 좌표 최신화

print(area)
